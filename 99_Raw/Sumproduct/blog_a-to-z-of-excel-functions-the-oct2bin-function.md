# A to Z of Excel Functions: The OCT2BIN Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oct2bin-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The OCT2BIN Function

*   March 26, 2023

A to Z of Excel Functions: The OCT2BIN Function
===============================================

A to Z of Excel Functions: The OCT2BIN Function
===============================================

27 March 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **OCT2BIN** function._

**The OCT2BIN function**

This function converts an octal number (base eight) to a binary number (base two).

![](https://sumproduct.com/wp-content/uploads/2025/05/650b2a8efaf180bbab2210f5701a2af9.jpg)

The **OCT2BIN** function employs the following syntax to operate:

**OCT2BIN(number,  
\[places\])**

The **OCT2BIN**function has the following arguments:

*   **number**:this is required and represents the octal number you wish to convert. It should be noted that **number** cannot contain more than 10 octal characters (30 bits) and that the most significant bit of **number** is the sign bit. The remaining 29 bits are magnitude bits. Negative numbers are represented using **two’s complement** notation
*   **places**:this is optional and represents the number of characters to use. If **places** is omitted, **OCT2BIN** uses the minimum number of characters necessary. The argument **places** is useful for padding the return value with leading 0s (zeroes).

**Two’s complement** is a mathematical operation on binary numbers, as well as a binary signed number representation based on this operation. The two’s complement of an **N**\-bit number is defined as the complement with respect to 2**N**; in other words, it is the result of subtracting the number from 2**N**. This is also equivalent to taking the ones’ complement and then adding one, since the sum of a number and its ones’ complement is all 1 bits. The two’s complement of a number behaves like the negative of the original number in most arithmetic, and positive and negative numbers can coexist in a natural way.

It should be further noted that:

*   if **number** is negative, **OCT2BIN** ignores **places** and returns a 10-character binary number
*   if **number** is negative, it cannot be less than 7777777000, and if **number** is positive, it cannot be greater than 777
*   If **number** is not a valid octal number, **OCT2BIN** returns the _#NUM!_ error value
*   if **OCT2BIN** requires more than **places** characters, it returns the _#NUM!_ error value
*   if **places** is not an integer, it is truncated
*   if **places** is nonnumeric, **OCT2BIN** returns the _#VALUE!_ error value
*   if **places** is negative, **OCT2BIN** returns the _#NUM!_ error value.

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/c39a29aed139c3916187676c35266d45.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oct2bin-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oct2bin-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oct2bin-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oct2bin-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oct2bin-function/#0 "close")

top
# A to Z of Excel Functions: The DEC2BIN Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-dec2bin-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The DEC2BIN Function

*   June 10, 2018

A to Z of Excel Functions: The DEC2BIN Function
===============================================

A to Z of Excel Functions: The DEC2BIN Function
===============================================

11 June 2018

This function converts a decimal number (base 10) to binary (base two).

The **DEC2BIN** function employs the following syntax to operate:

**DEC2BIN(number, \[places\])**

The **DEC2BIN** function has the following arguments:

*   **number:** this is required and represents the decimal integer you wish to convert. If **number** is negative, valid place values are ignored and **DEC2BIN** returns a 10-character (10-bit) binary number in which the most significant bit is the sign bit. The remaining 9 bits are magnitude bits. Negative numbers are represented using two’s-complement notation
*   **places:** this argument is optional. This is the number of characters to use. If **places** is omitted, **DEC2BIN** uses the minimum number of characters necessary. The argument **places** is useful for padding the return value with leading 0s (zeros).

**Two’s complement** is a mathematical operation on binary numbers, as well as a binary signed number representation based on this operation. The two’s complement of an **N**\-bit number is defined as the complement with respect to 2**N**; in other words, it is the result of subtracting the number from 2**N**. This is also equivalent to taking the ones’ complement and then adding one, since the sum of a number and its ones’ complement is all 1 bits. The two’s complement of a number behaves like the negative of the original number in most arithmetic, and positive and negative numbers can coexist in a natural way.

It should be further noted that:

*   if **number** < -512 or if **number** > 511, **DEC2BIN** returns the _#NUM!_ error value
*   if **number** is nonnumeric, **DEC2BIN** returns the _#VALUE!_ error value
*   if **DEC2BIN** requires more than **places** characters, it returns the _#NUM!_ error value
*   if **places** is not an integer, it is truncated
*   if **places** is non-numeric, **DEC2BIN** returns the _#VALUE!_ error value
*   if **places** is zero or negative, **DEC2BIN** returns the _#NUM!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-dec2bin-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-dec2bin-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-dec2bin-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-dec2bin-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-dec2bin-function/#0 "close")

top
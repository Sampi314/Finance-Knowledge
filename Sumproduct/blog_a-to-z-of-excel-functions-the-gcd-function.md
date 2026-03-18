# A to Z of Excel Functions: The GCD Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gcd-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The GCD Function

*   February 9, 2020

A to Z of Excel Functions: The GCD Function
===========================================

A to Z of Excel Functions: The GCD Function
===========================================

10 February 2020

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **GCD** function._

**The GCD function**

In mathematics, the greatest common divisor (GCD), also known as the greatest common denominator or the highest common factor, of two or more non-zero integers, is the largest positive integer that divides the numbers without a remainder. For example, the GCD of 180 and 48 is 12.

To show this, if we factorise the numbers down to primes:

180 = 2 x 2 x 3 x 3 x 5

48 = 2 x 2 x 2 x 2 x 3

Therefore, the prime numbers shared are:

![](https://sumproduct.com/wp-content/uploads/2025/05/a8028473803327e5c09e6d393584a88b.jpg)

2 x 2 x 3 = 12.

A much more efficient method is the Euclidean algorithm, which uses the division algorithm in combination with the observation that the GCD of two numbers also divides their difference:

*   Divide 180 by 48 is 3 remainder 36, so
*   Divide 48 by 36 is 1 remainder 12, so
*   Divide 36 by 12 is 3 with no remainder.

Therefore, 12 is the GCD of 180 and 48.

The Excel function **GCD** returns the greatest common divisor of two or more integers. The greatest common divisor is the largest integer that divides both **number1** and **number2** without a remainder. It has the following syntax:

**GCD(number1, \[number2\], …)**

The **GCD** function has the following arguments:

*   **number1**, **number2**, … where **number1** is required, and subsequent numbers are optional. There can be between one (1) and 255 numbers. If any value is not an integer, it is truncated.

It should be further noted that:

*   if any argument is nonnumeric, **GCD** returns the _#VALUE!_ error value
*   if any argument is less than zero, **GCD** returns the _#NUM!_ error value
*   one divides any value evenly
*   a prime number has only itself and one as divisors
*   if a parameter to **GCD** is >=2^53, **GCD** returns the _#NUM!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gcd-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gcd-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gcd-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gcd-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gcd-function/#0 "close")

top
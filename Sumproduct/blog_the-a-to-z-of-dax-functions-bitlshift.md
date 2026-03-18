# The A to Z of DAX Functions – BITLSHIFT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitlshift/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – BITLSHIFT

*   April 5, 2022

The A to Z of DAX Functions – BITLSHIFT
=======================================

Power Pivot Principles: The A to Z of DAX Functions – BITLSHIFT
===============================================================

5 April 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **BITLSHIFT**._

**_The BITLSHIFT function_**

It’s time for another of the most commonly used functions on the planet. If the planet is Uranus. This function returns a number shifted left by the specified number of bits. For those of us who have social lives, this means that you first convert the number to binary and then add on a specified number of zeros before converting the new binary number back to a decimal number.

The **BITLSHIFT** function employs the following syntax to operate:

**BITLSHIFT(number, shift\_amount)**

The **BITLSHIFT** function has the following arguments:

*   **number:** this is required, and must be any DAX expression that returns an integer expression
*   **shift\_amount:** this is also required. The **shift\_amount** must also be an integer.

It should be further noted that:

*   shifting a number left is equivalent to adding zeros (0) to the right of the binary representation of the number. For example, a two-bit shift to the left on the decimal value 4 converts its binary value (100) to 10000, or 16 in decimal
*   there is no limit on **number**, but the result may underflow / overflow
*   if the absolute value of **shift\_amount** is greater than 64, **BITLSHIFT** will return no error, but it will result in an underflow / overflow
*   a negative number used as the **shift\_amount** argument shifts the number of bits to the right
*   a negative number used as the **shift\_amount** argument returns the same result as a positive **shift\_amount** argument for the **BITRSHIFT** function.

Please see my example below:

![](<Base64-Image-Removed>)

In binary, 2 is 10, so this becomes 10**000**, which is 16 in decimal.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitlshift/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitlshift/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitlshift/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitlshift/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-bitlshift/#0 "close")

top
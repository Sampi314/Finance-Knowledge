# A to Z of Excel Functions: The GESTEP Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gestep-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The GESTEP Function

*   February 23, 2020

A to Z of Excel Functions: The GESTEP Function
==============================================

A to Z of Excel Functions: The GESTEP Function
==============================================

24 February 2020

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **GEOSTEP** function._

**The GESTEP function**

It may sound like some sort of military walk, but the **GESTEP** function was used to assist filtering out data. Imagine you wanted to identify data that exceeded or was equal to some hurdle (target value). If you are familiar with the IF function, you might create a calculation such as

**\=IF(value >= hurdle, 1, 0)**

In this case, if the variable **value** is greater than or equal to the **hurdle**, then a value of one (1) is returned, else zero (0). Well, guess what? There is a seemingly pointless Excel function out there that already does this for you. As a model auditor for more than 30 years, I can honestly say I have never seen the following function used in practice!

However, for completeness, the Excel function **GESTEP** returns one (1) if a compared number is greater than or equal to a “step;” (the given hurdle), otherwise it returns zero (0). This function may be used to filter a set of values. For example, by summing several **GESTEP** functions you can calculate the count of values that exceed a threshold.

**GESTEP** has the following syntax:

**GESTEP(number, \[step\])**

The **GESTEP** function has the following arguments:

*   **number:** this is required, and represents the value to test against the hurdle, **step**
*   **step:** this argument is optional. This is the threshold value; if this value is omitted, it is assumed to be zero (0).

It should be further noted that:

*   if any argument is nonnumeric, **GESTEP** returns the _#VALUE!_ error value.

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-269-1.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gestep-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gestep-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gestep-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gestep-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-gestep-function/#0 "close")

top
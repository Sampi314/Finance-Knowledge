# The A to Z of DAX Functions – CEILING

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ceiling/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CEILING

*   December 21, 2021

The A to Z of DAX Functions – CEILING
=====================================

Power Pivot Principles: The A to Z of DAX Functions – CEILING
=============================================================

21 December 2021

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at the **CEILING**…_

**_The CEILING function_**

Have you reached your **CEILING**? This function returns number rounded up, away from zero, to the nearest multiple of significance.

For example, if you are an American (which, let’s be honest is all Microsoft really cares about) and you want to avoid using cents in your prices (that makes no cents) and your product is priced at $12.24, use the formula **\=CEILING(**12.24**,** 0.05**)** to round prices up to the nearest nickel.

![](<Base64-Image-Removed>)

The **CEILING** function employs the following syntax to operate:

**CEILING(number, significance)**

It has two following arguments:

*   **number:** this is required and represents the value you wish to round or a column that contains values
*   **significance:** this is also required. This is the multiple used for rounding.

It should be further noted that:

*   regardless of the sign of **number**, a value is rounded up when adjusted away from zero. If **number** is an exact multiple of significance, no rounding occurs
*   if **number** is negative, and **significance** is negative, the value is rounded down, away from zero
*   if **number** is negative, and **significance** is positive, the value is rounded up towards zero
*   if either argument is non-numeric:

– a calculated column using **CEILING** will return _#ERROR_ values. For instance:

![](<Base64-Image-Removed>)

– a measure using **CEILING** will return a pop-up error warning message.

For example, we have a DAX measure below. Although both arguments are non-numeric, the ‘Check formula’ button does not recognise any error in the formula:

![](<Base64-Image-Removed>)

However, when the measure is used, one of the two error messages below will occur, depending upon whether **number** or **significance** is non-numeric.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

**_Examples_**

Example 1: The formula below will round 2.5 up to the nearest multiple of 1 and return 3.

![](<Base64-Image-Removed>)

Example 2: The formula below will round -2.5 up to the nearest multiple of -2 and return -4.

![](<Base64-Image-Removed>)

Example 3: The formula below will round -2.5 up to the nearest multiple of 2 and return -2.

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ceiling/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ceiling/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ceiling/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ceiling/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ceiling/#0 "close")

top
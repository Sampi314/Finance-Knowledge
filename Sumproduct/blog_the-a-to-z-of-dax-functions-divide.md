# The A to Z of DAX Functions – DIVIDE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-divide/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DIVIDE

*   June 6, 2023

The A to Z of DAX Functions – DIVIDE
====================================

Power Pivot Principles: The A to Z of DAX Functions – DIVIDE
============================================================

6 June 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **DIVIDE**._

**_The DIVIDE function_**

![](<Base64-Image-Removed>)

The **DIVIDE** function is one of the mathematical and trigonometric functions. It performs a division and returns the result or **BLANK()** on division by zero (_#DIV/0!)_. It has the following syntax:

**DIVIDE (numerator, denominator,  
alternate\_result)**

It has three \[3\] arguments in the syntax:

*   **numerator**: this is required, and it represents the number to divide (_i.e._ the **numerator**)
*   **denominator**: this is required, and it represents the number to divide by (_i.e._ the **denominator**)
*   **alternate\_result**: this is optional, and it represents the value returned when division by zero results in an error. If this argument is not stated, it will be set to a **BLANK** value as a default.

Here are a few remarks about this function:

*   the **alternative\_result** on divide by zero (_#DIV/0!_) must be a constant
*   the **DIVIDE** function is faster than an **IF** statement checking whether the denominator is zero \[0\], but the **DIVIDE** function is executed in the formula engine, and therefore it is not as fast as a native division.

Here are two simple examples of this function:

![](<Base64-Image-Removed>)

This will return:

![](<Base64-Image-Removed>)

Now let’s see the effect of dividing by zero \[0\]:

![](<Base64-Image-Removed>)

Which will return the string: “Infinity” as we specified in the **alternate\_result** argument.

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-divide/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-divide/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-divide/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-divide/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-divide/#0 "close")

top
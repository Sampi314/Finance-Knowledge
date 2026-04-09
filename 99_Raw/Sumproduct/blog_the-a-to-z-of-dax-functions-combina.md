# The A to Z of DAX Functions – COMBINA

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combina/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – COMBINA

*   May 17, 2022

The A to Z of DAX Functions – COMBINA
=====================================

Power Pivot Principles: The A to Z of DAX Functions – COMBINA
=============================================================

17 May 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **COMBINA**._

**_The COMBINA function_**

![](<Base64-Image-Removed>)

This function returns the number of combinations (with repetitions) for a given number of items. If this sounds a little confusing, think of it this way: you have a **number** of balls in the bag, each with a different number on it. You take one ball out at random, record its number, then replace it. You do this **number\_chosen** times. Ignoring the sequence of the numbers selected, **COMBINA** deduces the number of different combinations. Since there is replacement, **number\_chosen** may exceed the **number** too.

For example, selecting three numbers from a bag of balls numbered 1 to 4 would have the following 20 combinations:

111, 112, 113, 114, 122, 123, 124, 133, 134, 144, 222, 223, 224, 233, 234, 244, 333, 334, 344 and 444.

The **COMBINA** function employs the following syntax to operate:

**COMBINA(number, number\_chosen)**

The **COMBINA** function has the following arguments:

*   **number****:** this is required and must be greater than or equal to zero. Microsoft states that **number** must be greater than or equal to **number\_chosen** but this requirement does not seem to hold in practice (see my examples below)
*   **number\_chosen:** this is also required and Must be greater than or equal to zero too
*   non-integer values for both arguments will be truncated.

It should be further noted that:

*   if the value of either argument is outside of its constraints, **COMBINA** returns the _#NUM!_ error value
*   if either argument is a non-numeric value, **COMBINA** returns the _#VALUE!_ error value
*   the following equation is used:

![](<Base64-Image-Removed>)

*   in the equation above, **N** is **number** and **M** is **number\_chosen**
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Please see my example below:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Here, selecting four numbers from a bag of balls numbered 1 to 3 would have the following 15 combinations:

1111, 1112, 1113, 1122, 1123, 1133, 1222, 1223, 1233, 1333, 2222, 2223, 2233, 2333 and 3333.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combina/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combina/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combina/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combina/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-combina/#0 "close")

top
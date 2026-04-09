# The A to Z of DAX Functions – ATANH

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-atanh/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ATANH

*   September 28, 2021

The A to Z of DAX Functions – ATANH
===================================

Power Pivot Principles: The A to Z of DAX Functions – ATANH
===========================================================

28 September 2021

_In our long-established Power Pivot Principles articles, we are starting a new series on the A to Z of Data Analysis eXpression (DAX) functions. This week it’s all a load of hyperbolics…_

**_The ATANH function_**

Welcome to the wonderful world of “Functions You May Not Use in This or Your Next Life”. Today’s presentation is on the DAX function **ATANH**, which represents the inverse hyperbolic tangent function. That’s probably as far as I need to go, right…?

If like me, when you were at school you had a life rather than multiple maths lessons, inverse hyperbolic tangent functions may have passed you by. To understand let’s consider the following functions first:

![](<Base64-Image-Removed>)

and

![](<Base64-Image-Removed>)

These sorts of functions are used in differential equations and may also be used to derive trigonometric functions with complex arguments, _e.g._

![](<Base64-Image-Removed>)

and

![](<Base64-Image-Removed>)

The hyperbolic tangent function is defined (when **x** does not equal one \[1\]) as follows:

![](<Base64-Image-Removed>)

The inverse hyperbolic tangent function, **ATANH**, is the inverse of **tanh x** _(above)_, _i.e._

**ATANH(TANH(number)) = number**.

For a given value of a hyperbolic function, the corresponding inverse hyperbolic function provides the corresponding hyperbolic angle. The size of this hyperbolic angle is equal to the area of the corresponding hyperbolic sector of the hyperbola **xy****\= 1**, or twice the area of the corresponding sector of the unit hyperbola **x2 ? y2 = 1**, just as a circular angle is twice the area of the circular sector of the unit circle. Some call the inverse hyperbolic functions “area functions” as a consequence.

The syntax is straightforward:

**\=ATANH (number)**

There is only one argument:

*   **number:** the absolute value of which must not greater than one \[1\].

Please see my example below:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

You see? Who would have thought inverse hyperbolic tangents in Data Analysis eXpressions would be so easy!

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ _[here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
__._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-atanh/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-atanh/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-atanh/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-atanh/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-atanh/#0 "close")

top
# The A to Z of DAX Functions – COALESCE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coalesce/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – COALESCE

*   May 3, 2022

The A to Z of DAX Functions – COALESCE
======================================

Power Pivot Principles: The A to Z of DAX Functions – COALESCE
==============================================================

3 May 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **COALESCE**._

**_The COALESCE function_**

![](<Base64-Image-Removed>)

I’m drawing a bit of a **BLANK** with this one. Oh no, I remember. The **COALESCE** function returns the first expression that does not evaluate to **BLANK**. However, if all expressions evaluate to **BLANK**, then of course, **BLANK** is returned.

The **COALESCE** function employs the following syntax to operate:

**COALESCE(expression1, expression2 \[, expression 3, …\])**

The **COALESCE** function has the following arguments:

*   **expression1,** _etc_**:** the first arguments are required. These are any DAX expressions that return a scalar result. Expressions may be of different Data Types.

Please see my example below:

![](<Base64-Image-Removed>)

Returns the sum of all values in the **SalesAmount** column (field) in the **FactInternetSales** table, or else zero \[0\]. This is a particularly useful technique for converting **BLANK** values to zero \[0\].

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coalesce/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coalesce/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coalesce/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coalesce/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coalesce/#0 "close")

top
# The A to Z of DAX Functions – CLOSINGBALANCEQUARTER

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalancequarter/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CLOSINGBALANCEQUARTER

*   February 1, 2022

The A to Z of DAX Functions – CLOSINGBALANCEQUARTER
===================================================

Power Pivot Principles: The A to Z of DAX Functions – CLOSINGBALANCEQUARTER
===========================================================================

1 February 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **CLOSINGBALANCEQUARTER**._

**_The CLOSINGBALANCEQUARTER function_**

This function evaluates the expression at the last date of the quarter in a modified filter context. Its syntax is as follows:

**CLOSINGBALANCEQUARTER(expression, dates \[, filter\])**

It has several arguments:

*   **expression:** an expression that returns a scalar value
*   **dates:** a column that contains dates
*   **filter:** this is an optional Boolean expression or table expression that defines a filter.

It should be noted that:

*   **dates** argument can be any of the following:
    *   a reference to a date / time column
    *   a table expression that returns a single column of date / time values
    *   a Boolean expression that defines a single-column table of date / time values

*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

**_Example_**

We have a **Sales** table below containing sales transactions in 2021:

![](<Base64-Image-Removed>)

Now, we create a measure named **CBQuarter** that returns the amount at the last date of every quarter.

![](<Base64-Image-Removed>)

The result is as follows:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalancequarter/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalancequarter/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalancequarter/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalancequarter/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalancequarter/#0 "close")

top
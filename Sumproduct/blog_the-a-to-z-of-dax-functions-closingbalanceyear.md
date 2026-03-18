# The A to Z of DAX Functions – CLOSINGBALANCEYEAR

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalanceyear/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CLOSINGBALANCEYEAR

*   February 8, 2022

The A to Z of DAX Functions – CLOSINGBALANCEYEAR
================================================

Power Pivot Principles: The A to Z of DAX Functions – CLOSINGBALANCEYEAR
========================================================================

8 February 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **CLOSINGBALANCEYEAR**._

**_The CLOSINGBALANCEYEAR function_**

This function evaluates the expression at the last date of the year in a modified filter context. Its syntax is as follows:

**CLOSINGBALANCEYEAR(expression, dates \[, filter\]\[, year\_end\_date\])**

It has several arguments:

*   **expression:** an expression that returns a scalar value
*   **dates:** a column that contains dates
*   **filter:** this is an optional Boolean expression or table expression that defines a filter.
*   **year\_end\_date:** this is an optional literal string of the year-end date. The default is December 31. The year does not need to be included.

It should be noted that:

*   **year\_end\_date** argument is a literal string of a date in the same locale as the locale where it was created. The year portion is ignored
*   **dates** argument can be any of the following:
    *   a reference to a date / time column
    *   a table expression that returns a single column of date / time values
    *   a Boolean expression that defines a single-column table of date / time values
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

**_Example_**

We have a **Sales** table below containing sales transactions in 2021.

![](<Base64-Image-Removed>)

Let’s create a measure named **CBYear** that returns the amount at the last date of the financial year ended in June. Depending on the locale settings, you might have MM/DD or DD/MM format.

![](<Base64-Image-Removed>)

The result is as follows:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalanceyear/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalanceyear/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalanceyear/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalanceyear/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-closingbalanceyear/#0 "close")

top
# The A to Z of DAX Functions – AVERAGEX

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-averagex/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – AVERAGEX

*   October 19, 2021

The A to Z of DAX Functions – AVERAGEX
======================================

Power Pivot Principles: The A to Z of DAX Functions – AVERAGEX
==============================================================

19 October 2021

_In our long-established Power Pivot Principles articles, we are starting a new series on the A to Z of Data Analysis eXpression (DAX) functions. It’s another average function this time out…_

**_The AVERAGEX function_**

Today, we look at the **AVERAGEX** function. Like the **AVERAGE** function (discussed in our recent [_A to Z of Data Analysis eXpression (DAX) functions_ blog](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-az-average)
), this function calculates the average (arithmetic mean) of a set of expressions evaluated over a table.

The syntax is straightforward:

**\=AVERAGEX(table, expression)**

There are two arguments:

*   **table:** name of a table, or an expression that specifies the table over which the aggregation can be performed
*   **expression:** an expression with a scalar result, which will be evaluated for each row of the table in the first argument.

It should be further noted that:

*   the **AVERAGEX** function enables you to evaluate expressions for each row of a table, and then take the resulting set of values and calculate its arithmetic mean. Therefore, the function takes a **table** as its first argument, and an **expression** as the second argument
*   in all other respects, **AVERAGEX** follows the same rules as **AVERAGE**. You cannot include non-numeric or null cells. Both the **table** and **expression** arguments are required
*   when there are no rows to aggregate, the function returns a blank. When there are rows, but none of them meet the specified criteria, then the function returns zero \[0\]
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Please see my example below:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ _[here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
__._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-averagex/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-averagex/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-averagex/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-averagex/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-averagex/#0 "close")

top
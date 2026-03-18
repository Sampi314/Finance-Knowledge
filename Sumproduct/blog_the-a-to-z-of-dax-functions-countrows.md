# The A to Z of DAX Functions – COUNTROWS

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countrows/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – COUNTROWS

*   September 27, 2022

The A to Z of DAX Functions – COUNTROWS
=======================================

Power Pivot Principles: The A to Z of DAX Functions – COUNTROWS
===============================================================

27 September 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **COUNTROWS**._

**_The COUNTROWS function_**

The **COUNTROWS** function counts the number of rows in the specified table or in a table defined by an expression.

It employs the following syntax to operate:

**COUNTROWS(\[table\])**

The **COUNTROWS**function has just the one argument:

*   **table**: this argument is optional and represents the name of the **table** that contains the rows to be counted or an expression that returns a table. When it has not been provided, the default value is the home table of the current expression.

It should be further noted that:

*   the function returns a whole number (integer)
*   this function may be used to count the number of rows in a base table, but more often is used to count the number of rows that result from filtering a table, or applying context to a table
*   whenever there are no rows to aggregate, the function returns a blank. However, if there are rows, but none of them meet the specified criteria, the function returns zero \[0\]. Microsoft Excel also returns a zero if no rows are found that meet the conditions
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Sometimes, **COUNTROWS** is used when better syntax may be employed, _e.g._

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countrows/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countrows/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countrows/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countrows/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countrows/#0 "close")

top
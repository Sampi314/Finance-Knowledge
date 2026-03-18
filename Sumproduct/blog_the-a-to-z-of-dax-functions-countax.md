# The A to Z of DAX Functions – COUNTAX

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countax/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – COUNTAX

*   September 13, 2022

The A to Z of DAX Functions – COUNTAX
=====================================

Power Pivot Principles: The A to Z of DAX Functions – COUNTAX
=============================================================

13 September 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **COUNTAX**._

**_The COUNTAX function_**

Just when you thought this series had got the ax(e)…

This function counts the number of non-blank results when evaluating the result of an expression over a table. Not to be confused with the [COUNTA](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-counta)
 function that similarly counts non-blank results albeit in one column, this function iterates through the rows in a table and counts rows where a specified expression gives a non-blank result.

The **COUNTAX** function employs the following syntax to operate:

**COUNTAX(table, expression)**

The **COUNTAX** function has the following arguments:

*   **table:** this is required and represents the table containing the rows for which the expression will be evaluated
*   **expression**: this is also required and represents the expression to be evaluated for each row of the table.

It should be further noted that:

*   when the function finds no rows to aggregate, it returns a blank
*   the **COUNTAX** function counts cells containing any type of information, including other expressions. For example, if the column contains an expression that evaluates to an empty string, the **COUNTAX** function treats that result as non-blank. Usually, the **COUNTAX** function does not count empty cells but in this case the cell contains a formula, so it is counted
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Consider the following **Sales** Table:

![](<Base64-Image-Removed>)

We may create the following measure:

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

Do note how this works. If the DAX formula had been

**\=COUNTAX(Sales,  
Sales\[Target Achieved\] = “Yes”)**

the answer would have been six \[6\]. This is because the **COUNTAX** function counts the number of non-blank rows, not the number that contain “Yes”. Therefore, use **FILTER** to reduce the **Sales** Table to be just the rows where the target is achieved first (and then **COUNTAX** is counting the number of non-blank entries in the ‘**Sales Person**’ field.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countax/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countax/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countax/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countax/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-countax/#0 "close")

top
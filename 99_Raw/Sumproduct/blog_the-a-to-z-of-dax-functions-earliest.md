# The A to Z of DAX Functions – EARLIEST

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earliest/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – EARLIEST

*   July 11, 2023

The A to Z of DAX Functions – EARLIEST
======================================

Power Pivot Principles: The A to Z of DAX Functions – EARLIEST
==============================================================

11 July 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **EARLIEST**._

**_The_** _**EARLIEST**_ **_function_**

The **EARLIEST** function is one of the filter functions in DAX where it returns the current value of the specific column in an outer evaluation pass of the mentioned column. It employs the following syntax:

**EARLIEST(column)**

It only has one argument:

*   **column**: this is required and, represents a column or expression that result to a **column**.

It should be further noted that:

*   the **EARLIEST** function is similar to the **[EARLIER](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-earlier)
    ** function which allows you to specify one additional level of recursion
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

To illustrate the use of the **EARLIEST** function, consider the following example:

![](https://sumproduct.com/wp-content/uploads/2025/06/526b3c03a335a8ae35d19a85d928d5a8.jpg)

Here, we have the **Sales** table. We will create an aggregation measure for **SalesAmount** then we will use this aggregation along with the **EARLIEST** function to create a cumulative amount for each date, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/06/72f7468e5fa43db836b9c8d5e80cb1bb.jpg)

Next, we move to the Power Pivot data model there to create a calculated column with the following DAX code:

![](<Base64-Image-Removed>)

**EARLIEST\_Example:=CALCULATE(\[SalesAmount\],FILTER(Sales,Sales\[OrderDate\]<=****EARLIEST****(Sales\[OrderDate\])))**

This DAX code will return a cumulative **SalesAmount** by date:

![](<Base64-Image-Removed>)

However, similar to the **[EARLIER](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-earlier)
**function, if we use the same code in the calculated column to create a new measure, we will get an error message:

![](<Base64-Image-Removed>)

There is a workaround if you want to create measure instead of calculated column for the **EARLIEST** function:

![](<Base64-Image-Removed>)

**\=CALCULATE(**

      **SUM(Sales\[SalesAmount\]),**

      **FILTER(ALL(Sales),**

**SUMX(FILTER(Sales,****EARLIEST****(Sales\[OrderDate\])<=Sales\[OrderDate\]),Sales\[SalesAmount\])**

      **)**

      **)**

This DAX code help us replicate the same result we have in the previous example using calculated column for our measure. You can create a Pivot Table to view the result of the measure:

![](<Base64-Image-Removed>)

As we can see the result here is identical to the result using the calculated column in Power Pivot.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earliest/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earliest/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earliest/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earliest/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-earliest/#0 "close")

top
# The A to Z of DAX Functions – EFFECT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-effect/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – EFFECT

*   July 25, 2023

The A to Z of DAX Functions – EFFECT
====================================

Power Pivot Principles: The A to Z of DAX Functions – EFFECT
============================================================

25 July 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **EFFECT**._

**_The_** _**EFFECT**_ **_function_**

Does DAX sometimes not have the desired **EFFECT**? This function returns the effective annual interest rate, given the nominal annual interest rate and the number of compounding periods per year.

It employs the following syntax:

**EFFECT(nominal\_rate, npery)**

It has two \[2\] arguments in the syntax:

*   **nominal\_rate**: this is required and represents the nominal interest rate
*   **npery**: this is required and represents the number of compounding periods per year.

There are a few remarks for this function:

*   **EFFECT** which is short of the effective rate is calculated as follows:

![](https://sumproduct.com/wp-content/uploads/2025/06/bfebbeea07bed94ac7812e6a3ca12e55.jpg)

*   the **npery** argument is rounded to the nearest integer
*   an error is returned if:
    *   **nominal\_rate** ≤ 0
    *   **npery** < 1
*   the **EFFECT** function is not compatible with Power Pivot and currently it is only compatible with Power BI, SSAS Tabular, Azure AS and SSDT
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Consider a nominal interest rate of 5% and our **npery** is 12 months. Therefore, we will write the following DAX code to convert the nominal rate into the effective rate:

![](https://sumproduct.com/wp-content/uploads/2025/06/9705ba12183185bedbb79923d2da99cb.jpg)

We will have the following figure:

![](https://sumproduct.com/wp-content/uploads/2025/06/bb170e106487f2c28efc7895cc7c234f.jpg)

This is the effective rate after compounding twelve \[12\] times a year.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-effect/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-effect/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-effect/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-effect/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-effect/#0 "close")

top
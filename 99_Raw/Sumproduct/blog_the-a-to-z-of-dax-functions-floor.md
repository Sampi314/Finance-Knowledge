# The A to Z of DAX Functions – FLOOR

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-floor/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – FLOOR

*   December 26, 2023

The A to Z of DAX Functions – FLOOR
===================================

Power Pivot Principles: The A to Z of DAX Functions – FLOOR
===========================================================

26 December 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **FLOOR**._

**_The_** _**FLOOR**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/524f5da2b0f257b2e3b816ba1b7af341.jpg)

The _**FLOOR**_ functionis a **DAX** function which returns the results as text, rounded down to the nearest multiple of significance. It has the following syntax:

**FLOOR****(number, significance)**

*   **number**: this argument is required which is the number we want to round
*   **significance**: this is also required. This is the multiple to which you wish to round. Both the **number** and **significance** arguments need to have the same sign (_i.e._ both positive or else both negative).

It should be noted that:

*   if either argument is nonnumeric, the **FLOOR** function will return the _#VALUE!_ error
*   if **number** and **significance** arguments have different signs, the **FLOOR** function returns the _#NUM!_ error
*   a value is rounded down when it is adjusted away from zero, regardless of the sign of the number. No rounding takes place if the quantity is an exact multiple of the **significance**
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s consider the following example where we have the following **TB\_Grade** table:

![](<Base64-Image-Removed>)

We can write the following **DAX** measure to round these grades to the nearest 0, 0.25, 0.50, 0.75 as follows:

![](<Base64-Image-Removed>)

**FLOOR\_Example  
\= FLOOR(SUM(TB\_Grade\[Score\]), 0.25)**

This measure will return the following:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-floor/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-floor/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-floor/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-floor/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-floor/#0 "close")

top
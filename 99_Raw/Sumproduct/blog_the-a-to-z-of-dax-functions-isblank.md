# The A to Z of DAX Functions – ISBLANK

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isblank/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISBLANK

*   September 2, 2025

The A to Z of DAX Functions – ISBLANK
=====================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISBLANK**._

**_The_** _**ISBLANK**_ **_function_**

![](<Base64-Image-Removed>)

The **ISBLANK** function is one of information function that checks whether a value is blank and returns a Boolean value of TRUE if value is blank otherwise FALSE.

> **ISBLANK(value)**

There is one \[1\] main argument in this function:

*   **value**: this is the value or expression you want to test.

As an example, imagine you have a simple data like this in your Data Model with some blanks in the **Denominator** column.

![](<Base64-Image-Removed>)

Then you want to do quick divide between **Numerator** and **Denominator** by adding a column in the Data Model of Power Pivot.

![](<Base64-Image-Removed>)

To avoid _NaN_ and _∞_ when calculating, we can wrap everything in an **[IF](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-if/)
** with **ISBLANK** function to determine

> **IF(ISBLANK(\[Denominator\]),0,\[Numerator\]/\[Denominator\])**

![](<Base64-Image-Removed>)

This can help us error trapping the error seamlessly, although we can achieve the same the result with **[DIVIDE](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-divide/)
** function in this instance:

![](<Base64-Image-Removed>)

If we don’t specify the third argument of the **[DIVIDE](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-divide/)
** function, it will automatically generate a **[BLANK](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-blank/)
()** value where errors would otherwise be produced.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isblank/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isblank/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isblank/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isblank/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isblank/#0 "close")

top
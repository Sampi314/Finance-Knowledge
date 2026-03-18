# The A to Z of DAX Functions – ISBOOLEAN

**Source:** https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-isboolean/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISBOOLEAN

*   September 9, 2025

The A to Z of DAX Functions – ISBOOLEAN
=======================================

__In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISBOOLEAN**.__

**_**_The_** _**ISBOOLEAN**_ **_function_**_**

![](<Base64-Image-Removed>)

The **ISBOOLEAN** function is one of information function that checks whether a value Boolean (TRUE or FALSE) and returns a Boolean value of TRUE or FALSE.

**ISBOOLEAN(value)**

There is one \[1\] main argument in this function:

*   **value**: this is the value or expression you want to test.

Let’s test this function with few simple examples.

In the DAX query view of Power BI, we will write the following code to check if the number 14 is Boolean or not (hint: it isn’t!):

> **EVALUATE**
> 
>     **{ISBOOLEAN(14),}**

![](<Base64-Image-Removed>)

You will notice right away that the IntelliSense is flagging red all over the function but worry not it still allow you to run this function.

![](<Base64-Image-Removed>)

Let write a few more tests with TRUE, FALSE, one \[1\] and zero \[0\] values to see how this function evaluates each of them:

> **EVALUATE**
> 
>     **{ISBOOLEAN(14),**
> 
>      **ISBOOLEAN(TRUE),**
> 
>      **ISBOOLEAN(FALSE),**
> 
>      **ISBOOLEAN(1),**
> 
>      **ISBOOLEAN(0)}**

![](<Base64-Image-Removed>)

After clicking ‘Run’, only the Boolean values in lines 3 and 4 of the code line return TRUE while the rest return FALSE (which is correct).

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-isboolean/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-isboolean/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-isboolean/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-isboolean/#0)

[](https://sumproduct.com/blog/power-pivot-principles-the-a-to-z-of-dax-functions-isboolean/#0 "close")

top
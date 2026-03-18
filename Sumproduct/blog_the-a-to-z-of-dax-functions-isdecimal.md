# The A to Z of DAX Functions – ISDECIMAL

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdecimal/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISDECIMAL

*   September 30, 2025

The A to Z of DAX Functions – ISDECIMAL
=======================================

__In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISDECIMAL**.__

**_**_The_** _**ISDECIMAL**_ **_function_**_**

![](<Base64-Image-Removed>)

The **ISDECIMAL** function is one of the information functions that checks whether a value is a fixed precision decimal number (currency):

****ISDECIMAL(value)****

There is one \[1\] main argument in this function:

*   **value**: this is the **value** you want to test.

It should be noted that the **ISDECIMAL** function returns:

*   **TRUE**: if the expression evaluates to a fixed precision decimal number (currency)
*   **FALSE**: if the expression doesn’t evaluate to a fixed precision decimal number (currency).

Let’s consider the following example where we have the following dataset:

![](<Base64-Image-Removed>)

In the **Amount** column, the data is set as the ‘Decimal Number’ data type.

![](<Base64-Image-Removed>)

We can write the following query to create a new column **ValidAmount** to identify if **Amount** column is under the Fixed decimal number type:

**EVALUATE**

**ADDCOLUMNS(**

    **‘Transaction’,**

    **“ValidDate”, ISDECIMAL ( ‘Transaction'\[Amount\] )**

![](<Base64-Image-Removed>)

This will return the following table:

![](<Base64-Image-Removed>)

Let’s change the column type to a ‘Fixed decimal’ number:

![](<Base64-Image-Removed>)

If we run the same query, we can get the following table:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdecimal/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdecimal/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdecimal/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdecimal/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdecimal/#0 "close")

top
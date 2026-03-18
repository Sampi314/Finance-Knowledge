# The A to Z of DAX Functions – ISDATETIME

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdatetime/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISDATETIME

*   September 23, 2025

The A to Z of DAX Functions – ISDATETIME
========================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISDATETIME**._

**_The_** _**ISDATETIME**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/09/image-116.png)

The **ISDATETIME** function is one of the information functions that checks whether a value is a date / time:

**ISDATETIME(value)**

There is one \[1\] main argument in this function:

*   **value**: this is the **value** you want to test.

It should be noted that the **ISDATETIME** function returns:

*   **TRUE**: if the expression evaluates to a valid date / time
*   **FALSE**: if the expression doesn’t evaluate to a valid date / time.

Let’s consider the following example where we have the following dataset:

![](https://sumproduct.com/wp-content/uploads/2025/09/image-117.png)

In the **Date** column, some rows contain valid dates, while others are blank.  We can write the following query to create a new column **ValidDate** to flag invalid input:

**EVALUATE**

**ADDCOLUMNS(**

    **‘Transaction’,**

    **“ValidDate”, ISDATETIME ( ‘Transaction'\[Date\] )**

![](<Base64-Image-Removed>)

This will return the following table:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdatetime/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdatetime/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdatetime/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdatetime/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isdatetime/#0 "close")

top
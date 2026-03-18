# The A to Z of DAX Functions – COUNT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-count/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – COUNT

*   August 30, 2022

The A to Z of DAX Functions – COUNT
===================================

Power Pivot Principles: The A to Z of DAX Functions – COUNT
===========================================================

30 August 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **COUNT**._

**_The COUNT function_**

This function counts the number of rows in a specified column that contain any of the following kinds of values:

*   numbers
*   dates
*   strings.

The **COUNT** function employs the following syntax to operate:

**COUNT(column)**

The **COUNT** function has just the one argument:

*   **column:** this is required and represents the column (field) containing the values to be counted.

It should be further noted that:

*   when the function finds no rows to count, it returns a blank
*   blank values are skipped. TRUE / FALSE values are supposedly not supported, but do note the example below
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Consider the following Table called **Example**, with just the field, **List**:

![](https://sumproduct.com/wp-content/uploads/2025/06/51b23d982f3cd2b532daeac1ca3213fd.jpg)

Let’s create a simple measure:

![](https://sumproduct.com/wp-content/uploads/2025/06/26c1723c13063f7c76bd01eba1f5af2a.jpg)![](https://sumproduct.com/wp-content/uploads/2025/06/3cfd106d37bf4a9bb8779619dbefff12.jpg)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-count/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-count/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-count/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-count/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-count/#0 "close")

top
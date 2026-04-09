# The A to Z of DAX Functions – ISONORAFTER

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isonorafter/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISONORAFTER

*   January 6, 2026

The A to Z of DAX Functions – ISONORAFTER
=========================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISONORAFTER**._

**_The_** _**ISONORAFTER**_ **_function_**

![](<Base64-Image-Removed>)

The **ISONORAFTER** is a Boolean function that emulates the behaviour of a ‘Start At’ clause and returns TRUE for a row that meets all the conditions mentioned as parameters in this function:

**ISONORAFTER(scalar\_expression,** **scalar\_expression\[,** **sort\_order** **\[,** **scalar\_expression,** **scalar\_expression\[,** **sort\_order\]\]\]…)**

There are two \[2\] main arguments in this function:

*   **scalar** **expression**: this is any expression that returns a scalar value like a column reference or integer or string value.  Typically, the first parameter is a column reference and the second parameter is a scalar value
*   **sort** **order**: this is the order in which the column is sorted.  Can be ascending (ASC) or descending (DESC).  By default, the sort order is ascending.

Here are a few remarks about the **ISONORAFTER** function:

*   it is similar to **ISAFTER**.  The difference is **ISONORAFTER** returns true for values sorted on or after the filter values, whereas **ISAFTER** returns TRUE for values sorted strictly after the filter values
*   it is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

As an example, let’s say we have the following table named **Info**:

![](<Base64-Image-Removed>)

We want to return all rows that appear after the combination, including the row:

*   **Country/Region** = “AUS”
*   **State** = “VIC”.

when sorted alphabetically (ASC) on both columns.  Here is the **DAX** query code:

**`EVALUATE   FILTER (    Info,    ISONORAFTER(    Info[Country/Region], "AUS", ASC,    Info[State], "VIC", ASC)   )`**

![](<Base64-Image-Removed>)

This will return the following table:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isonorafter/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isonorafter/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isonorafter/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isonorafter/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isonorafter/#0 "close")

top
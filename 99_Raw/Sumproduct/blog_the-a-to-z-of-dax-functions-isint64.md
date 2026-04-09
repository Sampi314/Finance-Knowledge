# The A to Z of DAX Functions – ISINT64

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isint64/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – ISINT64

*   November 18, 2025

The A to Z of DAX Functions – ISINT64
=====================================

_____In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **ISINT64**._____

**_The_** _**ISINT64**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/10/image-197.png)

The **ISINT64** function is one of the information functions that examines whether a number is stored internally as an integer:

> **ISINT64(value)**

There is one \[1\] main argument in this function:

*   **value**: this is the value that the function performs the integer check on.

Here are a few remarks about the **ISINT64** function:

*   it returns TRUE when a value is stored as an integer in Power BI
*   it returns FALSE when a value is stored as anything other than an integer (for example decimal, text, currency) in Power BI
*   it has the same arguments and provides identical output as the **ISINTEGER** function
*   the largest and smallest number this function able to check is 9,223,372,036,854,775,807 and  -9,223,372,036,854,775,807 respectively
*   it is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s perform a test to see how the function operates under different conditions.  A table named **DataTypesWithChecks** was created which contains the data type used, its corresponding value and a check using **ISINT64**:

![](https://sumproduct.com/wp-content/uploads/2025/10/image-198.png)

**DataTypesWithChecks =**

**ADDCOLUMNS (**

    **ROW (**

        **“As Integer”,   42,**

        **“As Decimal”,   42.0,**

        **“As Currency”,  CURRENCY ( 42 ),**

        **“As Text”,      “42”**

    **),**

    **“Integer Check”,  ISINT64 ( \[As Integer\] ),**

    **“Decimal Check”,  ISINT64 ( \[As Decimal\] ),**

    **“Currency Check”, ISINT64 ( \[As Currency\] ),**

    **“Text Check”,     ISINT64 ( \[As Text\] )**

**)**

Each data type has been placed into separate columns as Power BI does not allow for variance of data types within the same column.  This is a better view of the data using visuals:

![](<Base64-Image-Removed>)

Notice, the **ISINT64** function has classified only the value entered in “As Integer” as an integer, whereas decimal, text or currency values are not deemed integers despite visually appearing as such.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isint64/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isint64/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isint64/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isint64/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-isint64/#0 "close")

top
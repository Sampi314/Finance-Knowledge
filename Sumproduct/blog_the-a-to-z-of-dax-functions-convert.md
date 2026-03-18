# The A to Z of DAX Functions – CONVERT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-convert/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CONVERT

*   July 26, 2022

The A to Z of DAX Functions – CONVERT
=====================================

Power Pivot Principles: The A to Z of DAX Functions – CONVERT
=============================================================

26 July 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **CONVERT**._

**_The CONVERT function_**

The **CONVERT** function is used to convert an expression of one Data Type to another. It employs the following syntax to operate:

**CONVERT(expression, datatype)**

*   **expression:** this is required. This is any valid DAX expression
*   **datatype:** also required, this represents an enumeration that includes:
    *   INTEGER (Whole Number)
    *   DOUBLE (Decimal Number)
    *   STRING (Text)
    *   BOOLEAN (TRUE / FALSE)
    *   CURRENCY (Fixed Decimal Number)
    *   DATETIME (Date, Time, _etc_.).

It should be further noted that:

*   the function returns an error when a value cannot be converted to the specified **datatype**
*   DAX calculated columns must be of a single data type. Since **MEDIAN** and **MEDIANX** functions over an integer column return mixed data types, either integer or double, the following calculated column expression will return an error as a result:

**MedianNumberCarsOwned = MEDIAN(DimCustomer\[NumberCarsOwned\])**

*   to avoid mixed **datatype**s, change the expression to always return the double Data Type, _e.g._

**MedianNumberCarsOwned = MEDIANX(DimCustomer, CONVERT(\[NumberCarsOwned\], DOUBLE))**

*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

The following DAX query

**EVALUATE { CONVERT(DATE(1900, 1, 1), INTEGER) }**

returns

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/blog/power-pivot-principles)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-convert/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-convert/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-convert/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-convert/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-convert/#0 "close")

top
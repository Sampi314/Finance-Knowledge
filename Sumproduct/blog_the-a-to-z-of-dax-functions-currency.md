# The A to Z of DAX Functions – CURRENCY

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currency/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – CURRENCY

*   December 20, 2022

The A to Z of DAX Functions – CURRENCY
======================================

Power Pivot Principles: The A to Z of DAX Functions – CURRENCY
==============================================================

20 December 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **CURRENCY**._

**_The CURRENCY function_**

The **CURRENCY** function is used to evaluate the value of an expression and return it in the currency data type. It employs the following syntax to operate:

**CURRENCY(value)**

*   **value**: this is required. Any DAX expression that returns a single scalar value.

It should be further noted that:

*   the **CURRENCY** function returns the fourth \[4th\] decimal digit by rounding up the fifth \[5th\] significant decimal in value; rounding up happens if the fifth \[5th\] significant decimal is equal to or greater than five \[5\]. For instance, the value of 9.012345 will return to 9.0123 after applying the **CURRENCY** function. However, if the value is 9.888888, then converting to currency returns 9.8889. As shown here:

![](https://sumproduct.com/wp-content/uploads/2025/06/0a17617c2fab81a6a384ae949ff177f1.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/d2d947aa159d9e5e30a78d53901389f7.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/5da8f62ccd98f09c249e0a0a98a4da39.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/0b0ebb60cd40cb415adfb51725463a37.jpg)

*   if the data type of the expression is Boolean (TRUE / FALSE), the **CURRENCY** function will return one \[1\] for TRUE and zero \[0\] for FALSE. For example:

![](https://sumproduct.com/wp-content/uploads/2025/06/305790b5f489f81aacf76f54baf39618.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/13fec9d24b0bfeb946d2d64e417e537c.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/31873d736cfa95d3b28a7387e9195c94.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/1896cf1afce7413dc5a749f8d0dfd412.jpg)

*   the **CURRENCY** function will attempt to convert a string to a number if the expression’s data type is Text; if the conversion is successful, the number will be converted to Currency; otherwise, an error is returned. For example:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

*   when the expression’s data type is DateTime, the **CURRENCY** function will convert the DateTime value into a number and then that number into Currency. DateTime values consist of a fractional component that reflects the fraction of a day (where 12 hours or noon is 0.5 days) and an integer part that counts the whole days between the specified date and 1900-03-01. An error will show up if the expression’s value is not a valid DateTime value

*   the **CURRENCY** function behaves similarly to using the [**CONVERT**](https://www.sumproduct.com/blog/article/power-pivot-principles/the-a-to-z-of-dax-functions-convert)
     function with Currency as the second argument. The two following claims are interchangeable:
    *   Expression using the **CURRENCY** function:

**EVALUATE {** 

**CURRENCY ( <expression> ) }**

*   *   Expression using the **CONVERT** function:

**EVALUATE {** 

**CONVERT ( <expression>, CURRENCY ) }**

Both of these DAX queries will produce the same result.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currency/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currency/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currency/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currency/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-currency/#0 "close")

top
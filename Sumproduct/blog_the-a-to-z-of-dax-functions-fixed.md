# The A to Z of DAX Functions – FIXED

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-fixed/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – FIXED

*   December 19, 2023

The A to Z of DAX Functions – FIXED
===================================

Power Pivot Principles: The A to Z of DAX Functions – FIXED
===========================================================

19 December 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **FIXED**._

**_The_** _**FIXED**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/a0a32c0ec2d2f2a121af55cea09ee976.jpg)

The _**FIXED**_ functionis one of the text functions which returns the text value after rounding a number to the designated number of decimals. You may also specify whether the result should be returned with or without commas. It has the following syntax:

**FIXED****(number, decimals, no\_commas)**

*   **number**: this argument is required and represents the number we wish to round and convert to text, or a column containing a number
*   **decimals**: this is optional. It is the number of digits to the right of the decimal point and the default value here is two \[2\] if this argument is omitted
*   **no\_commas**: this is optional. It is a logical value. If we put one \[1\], it will not display commas in the return text and will if we put zero \[0\] in this argument. If this argument is omitted, it will return text including commas.

It should be noted that:

*   if the value for **decimals** argument is negative, the **number** will be rounded to the left of the decimal point
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Let’s consider the following example where we have the following **TB\_Sales** table:

![](<Base64-Image-Removed>)

As we can see here, the **SalesAmount** column is displayed to four \[4\] decimal places and the number is right-aligned here. We will write the following **FIXED\_Example** measure:

![](https://sumproduct.com/wp-content/uploads/2025/06/fe4f27eddd86434a27c959e92fd6b4e0.jpg)

**FIXED\_Example  
\= FIXED(SUM(TB\_Sales\[SalesAmount\]))**

After we drag the **OrderDate** and the above measure in, you may be able to display something similar to the following:

![](https://sumproduct.com/wp-content/uploads/2025/06/1ea9156eaa675d9c960616ecba706188.jpg)

In this picture, the **OrderDate** is identical to the source data and the **SalesAmount** here is left-aligned, with rounding to two \[2\] decimal places.

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-fixed/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-fixed/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-fixed/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-fixed/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-fixed/#0 "close")

top
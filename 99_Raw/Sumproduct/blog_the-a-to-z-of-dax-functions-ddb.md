# The A to Z of DAX Functions – DDB

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ddb/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DDB

*   April 4, 2023

The A to Z of DAX Functions – DDB
=================================

Power Pivot Principles: The A to Z of DAX Functions – DDB
=========================================================

4 April 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at_ **_DDB_**_._

**_The DDB function_**

The **DDB** function is one of the financial functions. It returns the depreciation of an asset for a specified period using the double-declining balance method or some other method you specify. It has the following syntax:

**DDB(cost,  
salvage, life, period, \[factor\])**

It has five \[5\] arguments:

*   **cost**: this is required, and represents the initial cost of the asset
*   **salvage**: this is required, and represents the value of the asset at the end of depreciation
*   **life**: this is required, and is the number of periods over which the asset is to be depreciated
*   **period**: this is required, and is the period for which you want to calculate the depreciation. The period must use the same unit as life and its value should be between one \[1\] and **life** (inclusive)
*   **factor**: this component is optional and represents the rate at which the balance declines. If omitted, it is assumed to be two \[2\].

It should be further noted that:

*   the double-declining balance method calculates depreciation at an accelerated rate. Depreciation is highest in the first period and decreases in successive periods. The formula DDB uses is as follows:

![](<Base64-Image-Removed>)

*   **period** is rounded to the nearest integer
*   an error will occur if:
    *   **cost** or **salvage**< 0
    *   **life** or **period**< 1
    *   **period** > **life**
    *   **factor** ≤ 0.
*   the **DDB** function is not compatible with Power Pivot and currently it is only compatible with Power BI, SSAS Tabular, Azure AS and SSDT
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Suppose we have an initial asset that has value of 1,000,000 and zero \[0\] salvage value. The asset has a useful life of ten \[10\] years, and we have decided to use 1.5 as our depreciation factor. Suppose we want to know the depreciation for the fifth \[5th\] period. We can write the following DAX query:

![](<Base64-Image-Removed>)

This will return 78,300.9375: the depreciation charge in the fifth \[5th\] period, assuming a value of zero \[0\] after ten \[10\] years, using a factor of 1.5.

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ddb/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ddb/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ddb/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ddb/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-ddb/#0 "close")

top
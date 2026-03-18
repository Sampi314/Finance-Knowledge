# A to Z of Excel Functions: The DB Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-db-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The DB Function

*   April 29, 2018

A to Z of Excel Functions: The DB Function
==========================================

A to Z of Excel Functions: The DB Function
==========================================

30 April 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **DB** function._

**The DB function**

Depreciation is a method of allocating costs over the useful economic life of an asset (_e.g._ a building, a car, a computer). This function returns the depreciation of an asset for a specified period using what is known as the fixed-declining balance method _(explained below)_.

![](https://sumproduct.com/wp-content/uploads/2025/05/4669de9bab02fe078cd3875a0ec7c231.jpg)

Declining balance is a form of accelerated depreciation that will depreciate more aggressively than the straight-line method (where the same charge is applied in each period of equal length). This method is appropriate when an asset has higher functionality in the early years of use and becomes obsolete quickly. This method ensures that more depreciation is accounted for in the first few years, as a constant rate is applied to the remaining non-depreciated balance. Fixed assets such as computer equipment are a good example since they are typically only used for a couple of years and then replaced.

The **DB** function employs the following syntax to operate:

**DB(cost, salvage, life, period, \[month\])**

The **DB** function has the following arguments:

*   **cost:** this is required and represents the initial cost of the asset
*   **salvage:** this is also required. This is the value at the end of the depreciation (sometimes called the salvage value of the asset)
*   **life:** this is required. This is the number of periods over which the asset is being depreciated (sometimes called the useful life of the asset)
*   **period:** another variable required. This is the period for which you want to calculate the depreciation. The **period** must use the same units as **life**
*   **month:** this argument is optional and represents the number of months in the first year. If month is omitted, it is assumed to be 12 (the number of months in a year).

It should be further noted that:

*   the fixed-declining balance method computes depreciation at a fixed (_i.e._ constant) rate. **DB** uses the following formulae to calculate depreciation for a period:

(**cost – total depreciation from prior periods) \* rate**

where

**rate = 1 – ((salvage / cost) ^ (1 / life))**

*   rounded to three decimal places

*   Depreciation for the first and last periods is a special case. For the first period, **DB** uses this formula:

**cost \* rate \* month / 12**

*   For the last period, **DB** uses this formula:

**((cost – total depreciation from prior periods) \* rate \* (12 – month)) / 12**

Given rounding issues and the method of pro-rating, it should be noted that the depreciation will often not equal the amount to be depreciated at the end of the life _(see the example below)_. In financial modelling, you may need to calculate depreciation from first principles instead.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-db-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-db-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-db-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-db-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-db-function/#0 "close")

top
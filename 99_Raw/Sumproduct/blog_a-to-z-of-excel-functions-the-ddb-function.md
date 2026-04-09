# A to Z of Excel Functions: The DDB Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ddb-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The DDB Function

*   June 3, 2018

A to Z of Excel Functions: The DDB Function
===========================================

A to Z of Excel Functions: The DDB Function
===========================================

4 June 2018

**The DDB function**

Depreciation is a method of allocating costs over the useful economic life of an asset (_e.g._ a building, a car, a computer). This function returns the depreciation of an asset for a specified period using what is known as the fixed-declining balance method _(e__xplained below)_.

![](https://sumproduct.com/wp-content/uploads/2025/05/4a36a1f6e1bec89051f94d3fc30e05b5.jpg)

Declining balance is a form of accelerated depreciation that will depreciate more aggressively than the straight-line method (where the same charge is applied in each period of equal length). This method is appropriate when an asset has higher functionality in the early years of use and becomes obsolete quickly. This method ensures that more depreciation is accounted for in the first few years, as a constant rate is applied to the remaining non-depreciated balance. Fixed assets such as computer equipment are a good example since they are typically only used for a couple of years and then replaced.

This function returns the depreciation of an asset for a specified period using the double-declining balance method or some other method you specify.

The **DDB** function employs the following syntax to operate:

**DDB(cost, salvage, life, period, \[factor\])**

The **DDB** function has the following arguments:

*   **cost:** this is required and represents the initial cost of the asset
*   **salvage:** this is also required. This is the value at the end of the depreciation (sometimes called the salvage value of the asset). This value can be zero
*   **life:** this is required. This is the number of periods over which the asset is being depreciated (sometimes called the useful life of the asset)
*   **period:** another variable required. This is the period for which you want to calculate the depreciation. The **period** must use the same units as **life**
*   **factor:** this argument is optional. This is the rate at which the balance declines. If **factor** is omitted, it is assumed to be two (2) (the double-declining balance method)
*   **Important:** All five arguments must be positive numbers.

It should be further noted that:

*   the double-declining balance method computes depreciation at an accelerated rate. Depreciation is highest in the first period and decreases in successive periods. **DDB** uses the following formula to calculate depreciation for a period:
*   **Min**((**cost** – **total depreciation from prior periods**) \* (**factor** / **life**), (**cost** – **salvage** – **total depreciation from prior periods**))
*   Change **factor** if you do not want to use the double-declining balance method
*   Use the **VDB** function if you want to switch to the straight-line depreciation method when depreciation is greater than the declining balance calculation.Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/8ed35b07b2ef725975087ff201a863fa.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ddb-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ddb-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ddb-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ddb-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ddb-function/#0 "close")

top
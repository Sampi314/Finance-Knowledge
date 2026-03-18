# A to Z of Excel Functions: The DURATION Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-duration-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The DURATION Function

*   November 11, 2018

A to Z of Excel Functions: The DURATION Function
================================================

A to Z of Excel Functions: The DURATION Function
================================================

12 November 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **DURATION** function._

**The DURATION function**

The Macaulay Duration is a concept developed and named after Frederick Macaulay. It is measure of weighted average maturity of cash flows. Each cash flow weight can be found by dividing the present value of the cash flow by the price. The concept is commonly used by portfolio managers. Its formula is as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-534.jpg)

where:

*   **t** = respective time period
*   **C** = periodic coupon payment
*   **y** = periodic yield
*   **n** = total number of periods
*   **M** \= maturity value
*   **Current Bond Price** = present value of cash flows (time value of money).

This function returns the Macauley duration for an assumed par value of $100. The **duration** is defined as the weighted average of the present value of the cash flows and is used as a measure of a bond price’s response to changes in yield.

The **DURATION** function employs the following syntax to operate:

**DURATION(settlement, maturity, coupon, yield, frequency, \[basis\])**

The **DURATION** function has the following arguments:

*   **settlement:** this is required and represents the security’s **settlement** date. The security **settlement** date is the date after the issue date when the security is traded to the buyer
*   **maturity:** this is also required. This is the security’s maturity date. The maturity date is the date when the security expires
*   **coupon:** this is required. This is the security’s annual coupon rate
*   **yield:** again, this is required. This is the security’s annual yield
*   **frequency:** this is required and represents the number of coupon payments per year. For annual payments, frequency = 1; for semiannual, frequency = 2; for quarterly, frequency = 4
*   **basis:** this is optional. The type of day count basis to use, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/9d9803e1f8cb2977874ac0437ccc481e.jpg)

It should be further noted that:

*   Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2020 is serial number 43831 because it is 43,830 days after January 1, 1900
*   The **settlement** date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the **settlement** date would be July 1, 2008 and the maturity date would be January 1, 2038, which is 30 years after the January 1, 2008, issue date
*   **settlement**, **maturity**, **frequency**, and **basis** are truncated to integers
*   if **settlement** or **maturity** is not a valid date, **DURATION** returns the _#VALUE!_ error value
*   if **coupon** < 0 or if **yield** < 0, **DURATION** returns the _#NUM!_ error value
*   if **frequency** is any number other than 1, 2 or 4, **DURATION** returns the _#NUM!_ error value
*   if **basis** < 0 or if **basis** > 4, **DURATION** returns the _#NUM!_ error value
*   if **settlement** ≥ **maturity**, **DURATION** returns the _#NUM!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-duration-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-duration-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-duration-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-duration-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-duration-function/#0 "close")

top
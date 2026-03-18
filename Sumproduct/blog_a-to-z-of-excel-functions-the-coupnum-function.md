# A to Z of Excel Functions: The COUPNUM Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-coupnum-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The COUPNUM Function

*   February 1, 2018

A to Z of Excel Functions: The COUPNUM Function
===============================================

A to Z of Excel Functions: The COUPNUM Function
===============================================

2 February 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **COUPNUM** function._

**The COUPNUM function**

A coupon bond is a bond that pays interest before maturity. Once you own the bond, you can calculate the **num**ber of **coup**on payments you will receive over the life of the bond by using the **COUPNUM** function. Essentially, this function returns the number of coupons payable between the settlement date and maturity date, rounded up to the nearest whole coupon.

The **COUPNUM** function employs the following syntax to operate:

**COUPNUM(settlement, maturity, frequency, \[basis\])**

The **COUPNUM** function has the following arguments:

*   **settlement:** this represents the security’s settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer
*   **maturity:** this is the security’s maturity date, _i.e._ when the security expires
*   **frequency:** The number of coupon payments per year. For annual payments, **frequency** is 1; for semiannual, **frequency** is 2; for quarterly, **frequency** is 4_._ These are the only options _(see below)_
*   **basis:** the type of day count basis to use. This is optional. There are five options:

| Basis | Day count basis |
| --- | --- |
| **0** or omitted | US (NASD) 30 / 360 |
| **1** | Actual / actual |
| **2** | Actual / 360 |
| **3** | Actual / 365 |
| **4** | European 30 / 360 |

It should be further noted that:

*   Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900
*   dates should be entered using the **DATE** function, or as results of other formulae or functions. For example, use **\=DATE(2020,2,29)** for the 29th of February, 2020. Problems may occur if dates are entered as text
*   the settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, 30 years after the January 1, 2008, issue date
*   all arguments are truncated to integers
*   if **settlement** or **maturity** is not a valid date, **COUPNUM** returns the _#VALUE!_ error value
*   if **frequency** is any number other than 1, 2, or 4, **COUPNUM** returns the _#NUM!_ error value
*   if **basis** < 0 or if **basis** > 4, **COUPNUM** returns the _#NUM!_ error value
*   if **settlement** ≥ **maturity**, **COUPNUM** returns the _#NUM!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-coupnum-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-coupnum-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-coupnum-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-coupnum-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-coupnum-function/#0 "close")

top
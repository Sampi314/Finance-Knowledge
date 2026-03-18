# A to Z of Excel Functions: The INTRATE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-intrate-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The INTRATE Function

*   April 4, 2021

A to Z of Excel Functions: The INTRATE Function
===============================================

A to Z of Excel Functions: The INTRATE Function
===============================================

5 April 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **INTRATE** function._

**The INTRATE function**

First introduced in Excel 2007, the **INTRATE** function will calculate the interest rate for a fully invested security. For example, it is particularly useful in calculating the interest rate of an unlisted bond.

The **INTRATE** function employs the following syntax to operate:

**INTRATE(settlement, maturity, investment, redemption, \[basis\])**

The **INTRATE** function has the following arguments:

*   **settlement:** this represents the security’s settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer
*   **maturity:** this is the security’s maturity date, _i.e._ when the security expires
*   **investment:** this is the amount invested in the security
*   **redemption:** this is the amount to be received at **maturity**
*   **basis:** the type of day count basis to use. This is the only optional argument. There are five options:

![](https://sumproduct.com/wp-content/uploads/2025/05/9d17f1612f56c22a36007a1377b1042c.jpg)

It should be further noted that:

*   Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900
*   dates should be entered using the **DATE** function, or as results of other formulae or functions. For example, use **\=DATE(2020,2,29)** for the 29th of February, 2020. Problems may occur if dates are entered as text
*   the settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, 30 years after the January 1, 2008, issue date
*   **settlement**, **maturity** and **\[basis\]** are truncated to integers
*   if **settlement** or **maturity** is not a valid date, **INTRATE** returns the _#VALUE!_ error value
*   if **investment** ≤ 0 or if **redemption** ≤ 0, **INTRATE** returns the _#NUM!_ error value
*   if **basis** < 0 or if **basis** > 4, **INTRATE** returns the _#NUM!_ error value
*   if **settlement** ≥ **maturity**, **INTRATE** returns the _#NUM!_ error value
*   **INTRATE** is calculated as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/image2-1-1.gif)

where:

*   **B** \= number of days in a year, depending upon the **basis**
*   **DIM** \= number of days from **settlement** to **maturity**.

Please see my example below:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-227.jpg)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-intrate-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-intrate-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-intrate-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-intrate-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-intrate-function/#0 "close")

top
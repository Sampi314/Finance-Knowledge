# A to Z of Excel Functions: The RECEIVED Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-received-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The RECEIVED Function

*   August 11, 2024

A to Z of Excel Functions: The RECEIVED Function
================================================

A to Z of Excel Functions: The RECEIVED Function
================================================

12 August 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **RECEIVED** function._

**The RECEIVED function**

![](<Base64-Image-Removed>)

When you invest in a coupon bond, that is a bond that pays interest before maturity, you can evaluate your investment more accurately if you can make certain calculations. To find the amount you should receive at maturity for a fully invested security, you can use the **RECEIVED** function.

The **RECEIVED** function employs the following syntax to operate:

**RECEIVED(settlement, maturity, investment, discount, \[basis\])**

The **RECEIVED** function has the following arguments:

*   **settlement:** this is required and represents the security’s settlement date. The security settlement date is the date afterthe issue date when the security is traded to the buyer
*   **maturity:** this is also required and is the security’s maturity date, _i.e._ when the security expires
*   **investment:** this is required too, and is the amount invested in the security
*   **discount:** also required, this is the security’s discount rate
*   **basis:** the type of day count basis to use. This is optional. There are five options:

![](<Base64-Image-Removed>)

It should be further noted that:

*   Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900
*   dates should be entered using the **DATE** function, or as results of other formulae or functions. For example, use **\=DATE(2024,2,29)** for the 29th of February, 2024. Problems may occur if dates are entered as text
*   the settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six \[6\] months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, 30 years after the January 1, 2008, issue date
*   **settlement**, **maturity** and **basis** are truncated to integers
*   if **settlement** or **maturity** is not a valid date, **RECEIVED** returns the _#VALUE!_ error value
*   if **basis** < 0 or if **basis** > 4, **RECEIVED** returns the _#NUM!_ error value
*   if **settlement** ≥ **maturity**, **RECEIVED** returns the _#NUM!_ error value.

**RECEIVED** is calculated as follows:

![](<Base64-Image-Removed>)

where:

*   **DIM** \= number of days from issue to maturity
*   **B** \= number of days in a year, depending upon the basis.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._ _A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-received-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-received-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-received-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-received-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-received-function/#0 "close")

top
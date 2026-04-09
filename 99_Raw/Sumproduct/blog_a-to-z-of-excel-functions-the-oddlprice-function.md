# A to Z of Excel Functions: The ODDLPRICE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlprice-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The ODDLPRICE Function

*   May 21, 2023

A to Z of Excel Functions: The ODDLPRICE Function
=================================================

A to Z of Excel Functions: The ODDLPRICE Function
=================================================

22 May 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **ODDLPRICE** function._

**The ODDLPRICE function**

![](<Base64-Image-Removed>)

This one does an Oddjob _\[groan – Ed.\]_.

The **ODDLPRICE** function is an Excel financial function that calculates the price per $100 face value of a security or bond with an irregular last period. That’s what is meant by “odd”! The **L** isn’t an expression for where you end up if you were to use this function, but rather denoting this calculates for the **L**ast period.

In financial analysis, some bonds come with irregular first or last periods. Due to the irregular first or last period, the payment doesn’t fit in any of the usual or standard patterns. If you wish to calculate the price of a bond with an “odd” last period (either short or long), we can use the **ODDLPRICE** function.

The **ODDLPRICE** function employs the following syntax to operate:

**ODDLPRICE(settlement, maturity, last\_interest, rate, yield, redemption, frequency,  
\[basis\])**

The **ODDLPRICE** function has the following arguments:

*   **settlement:** this is required. This is the security’s settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer
*   **maturity:** this is also required. This represents the security’s maturity date. The maturity date is the date when the security expires
*   **last\_interest:** required. This denotes the security’s last coupon date

*   **rate:** yet again required. This is the security’s interest rate
*   **yield:** this is also required. This is the security’s annual yield
*   **redemption:** required. The security’s redemption value per $100 face value
*   **frequency:** also required. This considers the number of coupon payments per year. For annual payments, **frequenc**y = 1; for semiannual, **frequency** = 2; for quarterly, **frequency** = 4
*   **basis:** this last argument is the only one that is optional. This is the type of day count **basis** to use. There are five options:

![](<Base64-Image-Removed>)

It should be further noted that:

*   Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,447 days after January 1, 1900
*   dates should be entered using the **DATE** function, or as results of other formulae or functions. For example, use **\=DATE(2020,2,29)** for the 29th of February, 2020. Problems may occur if dates are entered as text
*   the **settlement** date is the date a buyer purchases a coupon, such as a bond. The **maturity** date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2024, and is purchased by a buyer six months later. The **issue** date would be January 1, 2024, the **settlement** date would be July 1, 2024, and the **maturity** date would be January 1, 2054, which is 30 years after the January 1, 2024, **issue** date
*   **settlement**, **maturity**, **last\_interest** and **basis** are all truncated to integers
*   if **settlement**, **maturity**, or **last\_interest** is not a valid date, **ODDLPRICE** returns the _#VALUE!_ error value
*   if **rate** < 0 or if **yield** < 0, **ODDLPRICE** returns the _#NUM!_ error value
*   if **basis** < 0 or if **basis** \> 4, **ODDLPRICE** returns the _#NUM!_ error value
*   the following date condition must be satisfied; otherwise, **ODDLPRICE** returns the _#NUM!_ error value:

**maturity** > **settlement** > **last\_interest**

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlprice-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlprice-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlprice-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlprice-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlprice-function/#0 "close")

top
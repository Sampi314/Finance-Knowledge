# A to Z of Excel Functions: The ODDLYIELD Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlyield-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The ODDLYIELD Function

*   June 4, 2023

A to Z of Excel Functions: The ODDLYIELD Function
=================================================

A to Z of Excel Functions: The ODDLYIELD Function
=================================================

5 June 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **ODDLYIELD** function._

**The ODDLYIELD function**

I always thought **ODDLYIELD** was the perfect collective noun for a group of financial modellers…

In financial analysis, some bonds come with irregular first or last periods. Due to the irregular first or last period, the payment doesn’t fit in any of the usual or standard patterns. If you wish to calculate the yield of a security with an “odd” **L**ast period (either short or long), we can use the **ODDLYIELD** function.

The **ODDLYIELD** function employs the following syntax to operate:

**ODDLYIELD(settlement, maturity, last\_interest, rate, price, redemption,  
frequency, \[basis\])**

The **ODDLYIELD** function has the following arguments:

*   **settlement:** this is required. This is the security’s settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer
*   **maturity:** this is also required. This represents the security’s maturity date. The maturity date is the date when the security expires
*   **last\_interest:** required. This denotes the security’s last coupon date
*   **rate:** yet again required. This is the security’s interest rate
*   **price:** this is also required. This is the security’s price
*   **redemption:** required. The security’s redemption value per $100 face value
*   **frequency:** also required. This considers the number of coupon payments per year. For annual payments, **frequenc**y = 1; for semiannual, **frequency** = 2; for quarterly, **frequency** = 4
*   **basis:** this last argument is the only one that is optional. This is the type of day count **basis** to use. There are five options:

![](https://sumproduct.com/wp-content/uploads/2025/05/7bad79345f6bc2bc4eb0c0b4a87c66df.jpg)

It should be further noted that:

*   Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,447 days after January 1, 1900
*   dates should be entered using the **DATE** function, or as results of other formulae or functions. For example, use **\=DATE(2020,2,29)** for the 29th of February, 2020. Problems may occur if dates are entered as text
*   the **settlement** date is the date a buyer purchases a coupon, such as a bond. The **maturity** date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2024, and is purchased by a buyer six months later. The **issue** date would be January 1, 2024, the **settlement** date would be July 1, 2024, and the **maturity** date would be January 1, 2054, which is 30 years after the January 1, 2024, **issue** date
*   **settlement**, **maturity**, **last\_interest** and **basis** are all truncated to integers
*   if **settlement**,**maturity** or **last\_interest** is not a valid date, **ODDLYIELD** returns the _#VALUE!_ error value
*   if **rate** < 0 or if **price** ≤ 0, **ODDLYIELD** returns the _#NUM!_ error value
*   if **basis** < 0 or if **basis** \> 4, **ODDLYIELD** returns the _#NUM!_ error value
*   the following date condition must be satisfied; otherwise, **ODDLYIELD** returns the _#NUM!_ error value:

**maturity** > **settlement** > **last\_interest**

*   **ODDLYIELD** is calculated as follows:

![](<Base64-Image-Removed>)

where:

*   **Ai** = number of accrued days for the **i**th, or last, quasi-coupon period within odd period counting forward from last interest date before **redemption**
*   **DCi** = number of days counted in the **i**th, or last, quasi-coupon period as delimited by the length of the actual coupon period

*   **NC** = number of quasi-coupon periods that fit in odd period (if this number contains a fraction, it is raised to the next whole number)
*   **NLi** = normal length in days of the **i**th, or last, quasi-coupon period within the odd coupon period.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlyield-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlyield-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlyield-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlyield-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-oddlyield-function/#0 "close")

top
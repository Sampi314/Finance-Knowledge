# The A to Z of DAX Functions – COUPNUM

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupnum/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – COUPNUM

*   November 8, 2022

The A to Z of DAX Functions – COUPNUM
=====================================

Power Pivot Principles: The A to Z of DAX Functions – COUPNUM
=============================================================

8 November 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **COUPNUM**._

**_The COUPNUM function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/acd375d797ae52111fd320fcae3f16e7.jpg)

A coupon bond is a bond that pays interest before maturity. Once you own the bond, you can calculate the **num**ber of **coup**on payments you will receive over the life of the bond by using the **COUPNUM** function. Essentially, this function returns the number of coupons payable between the settlement date and maturity date, rounded up to the nearest whole coupon.

The **COUPNUM** function employs the following syntax to operate:

**COUPNUM(settlement, maturity, frequency, \[basis\])**

The **COUPNUM**function has the following arguments:

*   **settlement:** this represents the security’s settlement date. The security settlement date is the date afterthe issue date when the security is traded to the buyer
*   **maturity:** this is the security’s maturity date, _i.e._ when the security expires
*   **frequency:** The number of coupon payments per year. For annual payments, **frequency** is 1; for semiannual, **frequency** is 2; for quarterly, **frequency** is 4_._ These are the only options _(see below)_
*   **basis:** the type of day count basis to use. This is optional. There are five options:

![](https://sumproduct.com/wp-content/uploads/2025/06/bbd6c4a5cbc346ad6b03514ac59e65c4.jpg)

It should be further noted that:

*   Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after December 30, 1899
*   dates should be entered using the **DATE** function, or as results of other formulae or functions. For example, use **\=DATE(2020,2,29)** for the 29th of February, 2020. Problems may occur if dates are entered as text
*   the settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, 30 years after the January 1, 2008, issue date
*   all arguments are truncated to integers
*   an error is returned if:  
    o **settlement** or **maturity** is not a valid date  
    o **frequency** is any number other than 1, 2, or 4  
    o **basis** < 0 or if **basis** \> 4  
    o **settlement** ≥ **maturity**

*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

Consider the following DAX example (not available in Power Pivot):

**EVALUATE  
{  
COUPNUM(DATE(2020, 1, 25), DATE(2021, 11,  
15), 2, 1)  
}**

This would return the number of coupon payments (**4**), where:

*   25 January 2020 is the settlement date
*   15 November 2021 is the maturity date
*   there are two \[2\] coupon payments per year (_i.e._ semi-annual coupon)
*   the day count basis used is an actual / actual basis.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupnum/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupnum/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupnum/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupnum/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupnum/#0 "close")

top
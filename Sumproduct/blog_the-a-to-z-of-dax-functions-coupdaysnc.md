# The A to Z of DAX Functions – COUPDAYSNC

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupdaysnc/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – COUPDAYSNC

*   October 25, 2022

The A to Z of DAX Functions – COUPDAYSNC
========================================

Power Pivot Principles: The A to Z of DAX Functions – COUPDAYSNC
================================================================

25 October 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **COUPDAYSNC**._

**_The COUPDAYSNC function_**

![](<Base64-Image-Removed>)

Coupon bonds pay interest at regular intervals, either one, two or four times a year. In DAX, you can use the **COUPDAYSNC**function to calculate the number of **coup**on **day**s from the **s**ettlement date to the **n**ext **c**oupon date.

The **COUPDAYSNC** function employs the following syntax to operate:

**COUPDAYSNC(settlement,  
maturity, frequency, \[basis\])**

The **COUPDAYSNC** function has the following arguments:

*   **settlement:** this represents the security’s settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer
*   **maturity:** this is the security’s maturity date, _i.e._ when the security expires
*   **frequency:** The number of coupon payments per year. For annual payments, **frequency** is 1; for semiannual, **frequency** is 2; for quarterly, **frequency** is 4_._ These are the only options _(see below)_
*   **basis:** the type of day count basis to use. This is optional. There are five options:

![](<Base64-Image-Removed>)

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
COUPDAYSNC(DATE(2020, 1, 25),  
DATE(2020, 11, 15), 2, 1)  
}**

This would return the number of days (**182**) from the settlement date to the next coupon date, where:

*   25 January 2020 is the settlement date
*   15 November 2020 is the maturity date
*   there are two \[2\] coupon payments per year (_i.e._ semi-annual coupon)
*   the day count basis used is an actual / actual basis.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupdaysnc/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupdaysnc/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupdaysnc/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupdaysnc/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-coupdaysnc/#0 "close")

top
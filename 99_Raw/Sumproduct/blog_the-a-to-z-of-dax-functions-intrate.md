# The A to Z of DAX Functions – INTRATE

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-intrate/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – INTRATE

*   August 5, 2025

The A to Z of DAX Functions – INTRATE
=====================================

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (**DAX**) functions.  This week, we look at **INTRATE**._

**_The_** _**INTRATE**_ **_function_**

![](<Base64-Image-Removed>)

The **INTRATE** function is one function that returns the interest rate for a fully invested security.

> **INTRATE(settlement, maturity, investment, redemption\[, basis\])**

There is five \[5\] main argument in this function:

*   **settlement**: this is the security’s settlement date.  The security settlement date is the date after the issue date when the security is traded to the buyer
*   **maturity:** this is the security’s maturity date.  The maturity date is the date when the security expires
*   **investment:** this is the amount invested in the security
*   **redemption:** this is the amount to be received at maturity
*   **basis:** (Optional) this is the type of day count basis to use.  If **basis** is omitted, it is assumed to be zero \[0\].  The accepted values are listed below this table:

![](<Base64-Image-Removed>)

Here are a few remarks about the **INTRATE** function:

*   dates are stored as sequential serial numbers so they can be used in calculations.  In **DAX**, December 30, 1899 is day 0, and January 1, 2008 is 39448 because it is 39,448 days after December 30, 1899  
      
    
*   the settlement date is the date a buyer purchases a coupon, such as a bond.  The maturity date is the date when a coupon expires.  For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later.  The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date is January 1, 2038, which is 30 years after the January 1, 2008, issue date  
      
    
*   **INTRATE** is calculated as follows:

![](<Base64-Image-Removed>)

where:

**B** = number of days in a year, depending on the year basis

**DIM** = number of days from settlement to maturity

*   **settlement** and **maturity** are truncated to integers  
      
    
*   **basis** is rounded to the nearest integer  
      
    
*   an error is returned if:
    *   **settlement** or maturity is not a valid date
    *   **settlement** ≥ **maturity**
    *   **investment** ≤ 0
    *   **redemption** ≤ 0
    *   **basis** < 0 or **basis** > 4  
          
        
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

As an example, we can write the following formula in DAX query view:

![](<Base64-Image-Removed>)

This means we invested $1,000,000 in the bond on 15 February 2020 and received $1,014,420 upon maturity on 15 May 2020, the formula returns the interest rate calculated on a 360-day basis.

This will return the discount rate for a bond using the terms specified above.

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section.  In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_.  If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-intrate/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-intrate/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-intrate/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-intrate/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-intrate/#0 "close")

top
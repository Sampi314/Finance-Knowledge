# A to Z of Excel Functions: The ISOWEEKNUM Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isoweeknum-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The ISOWEEKNUM Function

*   July 18, 2021

A to Z of Excel Functions: The ISOWEEKNUM Function
==================================================

A to Z of Excel Functions: The ISOWEEKNUM Function
==================================================

19 July 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **ISOWEEKNUM** function._

**The ISOWEEKNUM function**

![](<Base64-Image-Removed>)

The ISO week date system is effectively a leap week calendar system that is part of the ISO 8601 date and time standard issued by the International Organization for Standardization (ISO) since 1988 (last revised in 2004) and, before that, it was defined in ISO (R) 2015 since 1971. It is used (mainly) in government and business for fiscal years, as well as in timekeeping. This was previously known as “Industrial date coding”. The system specifies a week year atop the Gregorian calendar by defining a notation for ordinal weeks of the year.

An ISO week-numbering year (also called ISO year informally) has 52 or 53 full weeks. The extra week is sometimes referred to as a leap week, although ISO 8601 does not use this term.

Weeks start with Monday. Each week’s year is the Gregorian year in which the Thursday falls. The first week of the year, hence, always contains 4 January. ISO week year numbering therefore slightly deviates from the Gregorian for some days close to 1 January.

This function returns the number of the ISO week number of the year for a given date.

The **ISOWEEKNUM** function employs the following syntax to operate:

**ISOWEEKNUM(date)**

The **ISOWEEKNUM** function has the following arguments:

*   **date:** this is required and represents the date-time code used by Excel for date and time calculations.

It should be further noted that:

*   Microsoft Excel stores dates as sequential numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39,448 because it is 39,447 days after January 1, 1900
*   if the date argument is not a valid number, **ISOWEEKNUM** returns the _#NUM!_ error value
*   if the date argument is not a valid date type, **ISOWEEKNUM** returns the _#VALUE!_ error value.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found_ _[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
__._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isoweeknum-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isoweeknum-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isoweeknum-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isoweeknum-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-isoweeknum-function/#0 "close")

top
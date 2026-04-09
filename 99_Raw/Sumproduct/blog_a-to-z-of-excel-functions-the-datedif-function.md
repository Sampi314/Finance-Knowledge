# A to Z of Excel Functions: The DATEDIF Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datedif-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The DATEDIF Function

*   April 5, 2018

A to Z of Excel Functions: The DATEDIF Function
===============================================

A to Z of Excel Functions: The DATEDIF Function
===============================================

6 April 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **DATEDIF** function._

**The DATEDIF function**

This function has been described by past MVP Chip Pearson as “…the drunk cousin of the formula family…”. The **DATEDIF** function calculates the number of days, months or years between two dates. Excel provides the **DATEDIF** function in order to support older workbooks from Lotus 1-2-3 and may calculate incorrect results under certain scenarios _(see below)_. To use **DATEDIF**, you must type the function in manually; it will not appear to be recognised by Excel.

The **DATEDIF** function employs the following syntax to operate:

**DATEDIF(start\_date, end\_date, interval)**

The **DATEDIF** function has the following arguments:

*   **start\_date:** this is the date that represents the first, or starting, date of the period. Dates may be entered as text strings within quotation marks (for example, “17 Sep 1967”), as serial numbers (for example, 36921, which represents January 30, 2001, if you’re using the 1900 date system), or as the results of other formulas or functions (for example, **DATEVALUE(“1 Jan 2000”)**)
*   **end\_date****:** this is the date that represents the last, or ending, date of the period
*   **interval**: this must be entered and mandates whether the function should return the number of days (“d”), complete months (“m”) or complete years (“y”) between the two dates specified. The syntax for the interval is strict: the letters must be entered between inverted commas. In fact, the **interval** argument can also contain a combination of days, months and years in order to increase the variety of answers returned by the function. For example:
    *   “ym” – calculates the number of complete months between two dates as if the dates were in the same year
    *   “yd” – calculates the number of days between two dates as if the dates were in the same year
    *   “md” – calculates the number of days between two dates as if the dates were in the same month and year. Be careful with this option: Microsoft knows there are issues with this combination and does not recommend you relying on the results of this **interval**.

Watch out for two common error messages with this function:

_#VALUE!_ appears in the answer cell If one of **DATEDIF** ‘s arguments is not a valid date (_e.g._ the date was entered as text)

*   _#NUM!_ occurs in the result cell if the **start\_date** is larger (_i.e._ later in the year) than the **end\_date** argument.

It should be further noted that:

*   dates are stored as sequential serial numbers so they may be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,447 days after January 1, 1900
*   The **DATEDIF** function is useful in formulae where you need to calculate an age.

Please see my example below:

![](<Base64-Image-Removed>)

**_Known Issues_**

The “md” argument may result in a negative number, a zero or an inaccurate result. If you are trying to calculate the remaining days after the last completed month, you may need to revert to basic algebra using the **DAY** and **EOMONTH** (this determines the end of the month so many months from the date given) functions instead:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datedif-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datedif-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datedif-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datedif-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-datedif-function/#0 "close")

top
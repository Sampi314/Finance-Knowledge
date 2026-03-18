# A to Z of Excel Functions: The DATE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-date-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The DATE Function

*   April 1, 2018

A to Z of Excel Functions: The DATE Function
============================================

A to Z of Excel Functions: The DATE Function
============================================

2 April 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **DATE** function._

**The DATE function**

This function returns the sequential serial number that represents a particular date. Essentially, this was one method of avoiding the “dreaded Year 2000 bug” which concerned potential division by zero errors.

The **DATE** function employs the following syntax to operate:

**DATE(year,month,day)**

The **DATE** function has the following arguments:

*   **year:** thisis required. The value of the year argument can include one to four digits. Excel interprets the year argument according to the date system your computer is using. By default, Microsoft Excel for Windows uses the 1900 date system, which means the first date is January 1, 1900. It’s best to use four digits for the year argument to prevent unwanted results. For example, “18” could mean “1918” or “2018” – four-digit years prevent such confusion
    *   if **year** is between 0 (zero) and 1899 (inclusive), Excel adds that value to 1900 to calculate the year. For example, **DATE(108,1,2)** returns January 2, 2008 (1900+108)
    *   if **year** is between 1900 and 9999 (inclusive), Excel uses that value as the year. For example, **DATE(2008,1,2)** returns January 2, 2008
    *   if **year** is less than 0 or is 10000 or greater, Excel returns the _#NUM!_ error value
    *   **month:** this is also required and should be a positive or negative integer representing the month of the year from 1 to 12 (January to December)
    *   if **month** is greater than 12, **month** adds that number of months to the first month in the year specified. For example, **DATE(2018,14,2)** returns the serial number representing February 2, 2019
    *   if **month** is less than 1, **month** subtracts the magnitude of that number of months, plus 1, from the first month in the year specified. For example, **DATE(2018,-3,2)** returns the serial number representing September 2, 2017
*   **day:** again, this is required. This is a positive or negative integer representing the day of the month from 1 to 31
    *   if **day** is greater than the number of days in the month specified, **day** adds that number of days to the first day in the month. For example, **DATE(2018,1,35)** returns the serial number representing February 4, 2018
    *   if **day** is less than 1, **day** subtracts the magnitude that number of days, plus one, from the first day of the month specified. For example, **DATE(2018,1,-15)** returns the serial number representing December 16, 2017.

It should be further noted that:

*   Excel stores dates as sequential serial numbers so that they can be used in calculations. January 1, 1900 is serial number 1, and July 6, 2009 is serial number 40000 because it is 39,999 days after January 1, 1900
*   you will need to change the number format (**CTRL + 1**, ‘Format Cells’) in order to display a proper date
*   February 29, 1900 is recognised as day 60 on the 1900 date system. This date does not exist (years ending in “00” must be divisible by 400 to be a leap year), but this error has been perpetuated to be consistent / compatible with Lotus 1-2-3.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-date-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-date-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-date-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-date-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-date-function/#0 "close")

top
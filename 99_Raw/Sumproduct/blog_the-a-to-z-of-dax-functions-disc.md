# The A to Z of DAX Functions – DISC

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-disc/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DISC

*   May 2, 2023

The A to Z of DAX Functions – DISC
==================================

Power Pivot Principles: The A to Z of DAX Functions – DISC
==========================================================

2 May 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **DISC**._

**_The_** _**DISC**_ **_function_**

![](https://sumproduct.com/wp-content/uploads/2025/06/86c2c69fbee6c6a0a9aaea696f327e23.jpg)

The **DISC** function is one of financial function that returns the discount rate for a security. It has the following syntax:

**DISC(settlement, maturity, pr, redemption, \[basis\])**

It has five \[5\] arguments:

*   **settlement**: this is required and represents the security settlement date which is the date after the issue date when the security is traded to the buyer
*   **maturity**: this is required and represents the security maturity date which is the date when the security expires
*   **pr**: this is required. This is the security price per $100 face value
*   **redemption**: this is required. This is the security redemption value per $100 face value
*   **basis**: this is optional. This is the type of day count basis to use. If this argument is omitted, it will be set to the default value of zero \[0\]. There are five \[5\] acceptable values for this argument:
    *   0 or omitted: will use the US (NASD) 30 / 360 day-count convention
    *   1: will use the Actual / actual method which uses the actual number of days in each month and year to calculate the discount rate
    *   2: will use the Actual / 360 method which means that interest or any other relevant accrual factor will be calculated based on the actual number of days elapsed in a year of 360 days
    *   3: will use the Actual / 365 method which means that interest or any other relevant accrual factor will be calculated based on the actual number of days elapsed in a year of 365 days
    *   4: will use the Eurobond 30 / 360 day-count convention.

It should be noted that:

*   the dates will be stored as sequential serial numbers so that they can be used in calculations. 30 December 1899 will be day zero \[0\] in DAX
*   there are 3 different key dates which we should note here:
    *   **issue**: the date the bond or coupon is issued
    *   **settlement**: the date a buyer purchases the coupon or bond
    *   **maturity**: the date the bond or coupon expires
    *   for example, there is a 30-year bond issued on 1stJanuary 2020, and this bond is purchased by a buyer six \[6\] months later. Hence, 1st July 2020 is the settlement date, and the issue date would be 1st January 2020. The maturity date should be 1stJanuary 2050 which is 30 years after the issue date.
*   the **DISC** function will be computed as follows:

![](<Base64-Image-Removed>)

*   where:
    *   **B**: number of days in a year, depending on the year basis
    *   **DSM**: number of days between settlement and maturity date.
*   the **settlement** and **maturity** date are shortened to integers
*   the **basis** is rounded to the nearest integer
*   an error is returned if:
    *   **settlement** or **maturity** is not a valid date
    *   **settlement** ≥ **maturity**
    *   **pr** ≤ 0
    *   **redemption** ≤ 0
    *   **basis** <0 or **basis** > 4.
*   the **DISC** function is not compatible with Power Pivot and currently it is only compatible with Power BI, SSAS Tabular, Azure AS and SSDT
*   this function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.

As an example, we have the following data:

![](<Base64-Image-Removed>)

In this example, we will test out the effect of the basis so we will create five \[5\] different measures with the following DAX codes:

**DISC\_Example\_0  
\= {DISC(DATE(2018,7,1), DATE(2028,1,1), 90, 100, 0)}**

**DISC\_Example\_1  
\= {DISC(DATE(2018,7,1), DATE(2028,1,1), 90, 100, 1)}**

**DISC\_Example\_2  
\= {DISC(DATE(2018,7,1), DATE(2028,1,1), 90, 100, 2)}**

**DISC\_Example\_3  
\= {DISC(DATE(2018,7,1), DATE(2028,1,1), 90, 100, 3)}**

**DISC\_Example\_4  
\= {DISC(DATE(2018,7,1), DATE(2028,1,1), 90, 100, 4)}**

Which results in:

![](<Base64-Image-Removed>)

The results here is closely related to the way we count the day in the period. If the basis we selected has a high day count, it will result in a higher discount rate. For instance, we expect that the day count basis number two \[2\] will produce the lowest discount rate as this has the lowest day count when compared to other date count methods. The basis zero \[0\] and four \[4\] have the highest, because the US and EU 30 / 360 day-count methods add one \[1\] or two \[2\] days each year for February to round it up to 30 days which will result in a higher day count than the actual day count method. Thus, we have the following expression:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-disc/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-disc/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-disc/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-disc/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-disc/#0 "close")

top
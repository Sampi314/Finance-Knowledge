# The A to Z of DAX Functions – DATEDIFF

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datediff/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – DATEDIFF

*   January 31, 2023

The A to Z of DAX Functions – DATEDIFF
======================================

Power Pivot Principles: The A to Z of DAX Functions – DATEDIFF
==============================================================

31 January 2023

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at_ **_DATEDIFF_**_._

**_The DATEDIFF function_**

The **DATEDIFF** function is one of the Date and Time functions. It returns the number of interval boundaries between two dates. It operates using the following syntax:

**DATEDIFF(date1,  
date2, interval)**

There are three \[3\] arguments in this syntax:

*   **date1**: this is required, and must be a scalar datetime value
*   **date2**:this is also required, and also must be a scalar datetime value
*   **interval**:this argument is required, and it is the interval to use when comparing dates. The value can be one of the following: SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, QUARTER, or YEAR.

There are a few key notes about this function:

*   The result will be positive if **date2** is larger than **date1**
*   In previous versions of the DAX engine (earlier than 2018), this could provide an error if **date1** is larger than **date2**.

We can use **DATEDIFF** to calculate the difference between 1 January 2020 and 15 December 2022 in years, quarters, months, and days. First, we write the following DAX query:

**EVALUATE**

**VAR StartDate =  DATE ( 2020, 01, 01 )**

**VAR EndDate =    DATE ( 2022, 12, 15 )**

**RETURN**

**{**

**( “DATEDIFF Year”,     DATEDIFF ( StartDate, EndDate, YEAR )),**

**( “DATEDIFF  
Quarter”,  DATEDIFF ( StartDate, EndDate,  
QUARTER )),**

**( “DATEDIFF Month”,    DATEDIFF ( StartDate, EndDate, MONTH )),**

**( “DATEDIFF Day”,      DATEDIFF ( StartDate, EndDate, DAY ))**

**}**

![](<Base64-Image-Removed>)

This will yield the following result:

![](<Base64-Image-Removed>)

Alternatively, you can consider this example in Power Pivot where we have a table named **Date\_Table**:

![](<Base64-Image-Removed>)

Then we write the following DAX expression to calculate the difference in days, months and years between **Start Date** and **End Date**:

**Days Difference   := DATEDIFF(Date\_Table\[Start  \
Date\], Date\_Table\[End Date\], DAY)**

**Months Difference :=  
DATEDIFF(Date\_Table\[Start Date\], Date\_Table\[End Date\], MONTH)**

**Years Difference  :=  
DATEDIFF(Date\_Table\[Start Date\], Date\_Table\[End Date\], YEAR)**

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

The final result will be as follows:

![](<Base64-Image-Removed>)

_Come back next week for our next post on Power Pivot in the_ [_Blog_](https://www.sumproduct.com/blog)
 _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datediff/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datediff/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datediff/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datediff/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-datediff/#0 "close")

top
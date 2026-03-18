# Power BI Blog: New Way of Expressing Date and DateTime Values

**Source:** https://sumproduct.com/blog/power-bi-blog-new-way-of-expressing-date-and-datetime-values/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: New Way of Expressing Date and DateTime Values

*   September 8, 2021

Power BI Blog: New Way of Expressing Date and DateTime Values
=============================================================

Power BI Blog: New Way of Expressing Date and DateTime Values
=============================================================

9 September 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we review a new way to express Date and DateTime values with the latest Power BI update._

Microsoft is introducing a new way to express Date and DateTime-typed values as what is known as a _DAX literal_.

This will allow you to directly specify dates and times (up to the second) in you DAX queries, without having to use other functions. Starting with this latest release, Power BI now supports either a complete date value or a complete date and time value. The syntax is as follows:

Date format: **dt”YYYY-MM-DD”**

For example, **dt”1999-12-31?** would represent 31 December 1999.

Furthermore, the DateTime format is as follows:

DateTime format: **dt”YYYY-MM-DDThh:mm:ss”**

_or_

DateTime format: **dt”YYYY-MM-DD hh:mm:ss”**

For examples, **dt”2021-05-24T12:00:00?** and **dt”2021-05-24 12:00:00?** would both represent noon on 24 May 2021.

It should be noted that in these instances, DAX supports valid date / time components with fewer digits than indicated for ease of use, _e.g._ January may be specified as either “1” or “01”.

To show how this makes things simpler, consider the following example, where in the past you may have filtered sales to within a specific order date range by using the following DAX code:

**EVALUATE**

**FILTER (Sales, \[OrderDate\] > (DATE(2015,1,9) + TIME(2,30,0)) && \[OrderDate\] < (DATE(2015,12,31) + TIME(11,59,59)))**

This now simplifies to

**EVALUATE**

**FILTER (Sales, \[OrderDate\] > dt”2015-1-9T02:30:00″ && \[OrderDate\] < dt”2015-12-31T11:59:59″)**.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-new-way-of-expressing-date-and-datetime-values/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-new-way-of-expressing-date-and-datetime-values/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-new-way-of-expressing-date-and-datetime-values/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-new-way-of-expressing-date-and-datetime-values/#0)

[](https://sumproduct.com/blog/power-bi-blog-new-way-of-expressing-date-and-datetime-values/#0 "close")

top
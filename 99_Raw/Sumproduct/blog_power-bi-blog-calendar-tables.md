# Power BI Blog: CALENDAR tables

**Source:** https://sumproduct.com/blog/power-bi-blog-calendar-tables/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: CALENDAR tables

*   June 23, 2021

Power BI Blog: CALENDAR tables
==============================

Power BI Blog: CALENDAR tables
==============================

24 June 2021

Welcome back to this week’s edition of the Power BI blog series. This week, we will look at dynamic calendars that we can use for our analysis.

There are several ways to make a calendar table in Power BI – notably, using the Power Query side, and by creating a DAX table. We’ve previously covered how to do it in Power Query in other [blogs](https://www.sumproduct.com/thought/power-query-blog-series)
 – this time, we’re going to talk about using the **CALENDAR** function to create a DAX table instead.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-174.jpg)

First of all, we need to create a new table.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-229.jpg)

We can then name the table appropriately, and use the **CALENDAR** function. This function has two parameters – a start date and an end date. Essentially, the **CALENDAR** function will create a table that fills in the days between the start and end dates.

To make this dynamic, so that it points to the start and end of our dataset, we can link this back to the **MIN** and **MAX** of our relevant date fields:

**Calendar = CALENDAR(MIN(Transactions\[Transaction Date\]),MAX(Transactions\[Transaction Date\]))**

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-184.jpg)

From there, you can add on any additional columns you might need, such as the Year, Month, Day, and so on.

If you’re feeling particularly brave, you can try to use the **CALENDARAUTO** function, which will look through your dataset and try to find the appropriate dates to use:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-179.jpg)

Of course, if you happen to have birthdays of customers in your dataset, then it may end up choosing an inappropriate value as your minimum, resulting in a far larger calendar table than required.

**CALENDARAUTO** does give you the ability to easily set the start and end dates of a particular year using the optional FiscalYearEndMonth parameter, that will ensure that dates start and end at the start and end of the fiscal year (by default it will use calendar years, or an equivalent value of 12):

![](<Base64-Image-Removed>)

To do the equivalent using the **CALENDAR** function, you can use a combination of **DATE** and the **MIN/MAX** functions, like the following:

**Calendar = CALENDAR(DATE(YEAR(MIN(Transactions\[Transaction Date\])),1,1),DATE(YEAR(MAX(Transactions\[Transaction Date\])),12,31))**

There you have it! Easy calendar tables that don’t require you to code in M.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-calendar-tables/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-calendar-tables/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-calendar-tables/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-calendar-tables/#0)

[](https://sumproduct.com/blog/power-bi-blog-calendar-tables/#0 "close")

top
# Power Query: End of Dates

**Source:** https://sumproduct.com/blog/power-query-end-of-dates/

---

[Home](https://sumproduct.com/)

\> Power Query: End of Dates

*   July 10, 2018

Power Query: End of Dates
=========================

Power Query: End of Dates
=========================

11 July 2018

_Welcome to our Power Query blog. This week, I look at some ways to determine the end (and the start) of a particular date period in M._

I will take a look at some **Date() M** functions that can be used to return a date / time that represents the end or beginning of a particular period containing that data – for example, the end of the current year. Since these functions come in pairs (end and start for each time period), I will look at them in pairs, and give an example for each pair of functions. I am including these functions in my mini-series on dates mainly because they can be useful in calculations. These functions are also available under the ‘Date’ dropdown in the ‘Add Column’ tab from the Power Query Editor screen, but however they are called, it’s important to know what value is returned in order to use them correctly.

**_Date.StartOfMonth_** **_and_** **_Date.EndOfMonth_**

**Date****.StartOfMonth(datetime** **as** **nullable datetime)** **as** **nullable datetime**

Returns a datetime value representing the start of the month that contains **datetime**.

**Date****.EndOfMonth(datetime** **as** **nullable datetime)** **as** **nullable datetime**

Returns a datetime value for the end of the month that contains **datetime**.

I can look at the start and end of the month containing the final payment date:

![](https://sumproduct.com/wp-content/uploads/2025/05/19bb3322ba480db9445dd3ee04f40cee.jpg)

I can create two new columns, one for the start of the final payment month and one for the end. The **M** formulae I have used are:

**\= Date.StartOfMonth(\[Final Payment\])**

**\= Date.EndOfMonth(\[Final Payment\])**

![](https://sumproduct.com/wp-content/uploads/2025/05/8c1f541b215f1415638c2ddae7d5e3b9.jpg)

I can see that the function returns the time for the start date and end date of the month as 00:00:00, so I can allow for this in any calculations.

**_Date.StartOfQuarter_** **_and_** **_Date.EndOfQuarter_**

**Date****.StartOfQuarter****(****datetime****)**

Returns a datetime value representing the start of the quarter containing **datetime**.

**Date****.EndOfQuarter****(****datetime****)**

Returns a datetime value representing the end of the quarter containing **datetime**.

I can look at the start and end of the month containing the final payment date, and to do this I will create two new columns.

![](<Base64-Image-Removed>)

The **M** formulae I have used are:

**\= Date.StartOfQuarter(\[Final Payment\])**

**\= Date.EndOfQuarter(\[Final Payment\])**

I can then see the start and end of the financial quarter that the final payment takes place in.

**_Date.StartOfWeek_** **_and_** **_Date.EndOfWeek_**

**Date****.StartOfWeek(datetime** **as** **nullable datetime,** **optional** **firstday** **as** **nullable number)** **as** **nullable datetime**

Returns a datetime value representing the start of the week containing **datetime**.

**Date****.StartOfWeek(datetime** **as** **any,** **optional** **firstday** **as** **nullable number)** **as** **any**

Returns a datetime value for the end of the week containing **datetime**.

I have a little more flexibility here, as I can decide what day the week starts on using the value **firstday** as I did last week (please see [Power Query: Getting Something Out of a Date](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-getting-something-out-of-a-date)
) with the function **Date.DayOf Week()**.

Valid values are: **Day.Sunday**, **Day.Monday**, **Day.Tuesday**, **Day.Wednesday**, **Day.Thursday**, **Day.Friday**, and **Day.Saturday**. If I don’t specify a **firstday** then the default is Monday.

I will look at the start and end date of the week that final payment takes place by adding two columns.

![](<Base64-Image-Removed>)

The **M** formulae I have used are:

**\= Date.StartOfWeek(\[Final Payment\])**

**\= Date.EndOfWeek(\[Final Payment\])**

I have taken the default start of the week, which is Monday. It’s important to note that the end of week date also defaults to a Monday, which will affect any calculations. The end of week day will be the same as the start of week day, so if I change the end of week step to use Sunday as the start of the week,

![](<Base64-Image-Removed>)

the end of the week date is now a Sunday too.

**_Date.StartOfYear_** **_and_** **_Date.EndOfYear_**

**Date****.StartOfYear(datetime** **as** **nullable datetime)** **as** **nullable datetime**

Returns a datetime value representing the start of the year containing **datetime**.

**Date****.EndOfYear(datetime** **as** **nullable datetime)** **as** **nullable datetime**

Returns a datetime value for the end of the year containing **datetime**.

I will look at the start and end date of the year that final payment takes place by adding two columns.

![](<Base64-Image-Removed>)

The **M** formulae I have used are:

**\= Date.StartOfYear(\[Final Payment\])**

**\= Date.EndOfYear(\[Final Payment\])**

It’s useful to know that the end of the year here is actually the first day of the next year, which is important when constructing calculations.

**_Date.StartOfDay_** **_and_** **_Date.EndOfDay_**

**Date****.StartOfDay(datetime** **as** **nullable datetime)** **as** **nullable datetime**

Returns a datetime value for the start of the date of **datetime**.

**Date****.EndOfDay(datetime** **as** **nullable datetime)** **as** **nullable datetime**

Returns a datetime value for the end of the date of **datetime**.

I will look at the start and end of the date that final payment takes place by adding two columns.

![](<Base64-Image-Removed>)

The **M** formulae I have used are:

**\= Date.StartOfDay(\[Final Payment\])**

**\= Date.EndOfDay(\[Final Payment\])**

I can see that the end of day function actually gives me the start of the next day, which I would need to know if I included it in a calculation.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-end-of-dates/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-end-of-dates/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-end-of-dates/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-end-of-dates/#0)

[](https://sumproduct.com/blog/power-query-end-of-dates/#0 "close")

top
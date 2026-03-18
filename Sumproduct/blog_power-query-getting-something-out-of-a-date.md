# Power Query: Getting Something Out of a Date

**Source:** https://sumproduct.com/blog/power-query-getting-something-out-of-a-date/

---

[Home](https://sumproduct.com/)

\> Power Query: Getting Something Out of a Date

*   July 3, 2018

Power Query: Getting Something Out of a Date
============================================

Power Query: Getting Something Out of a Date
============================================

4 July 2018

_Welcome to our Power Query blog. This week, I look at some useful ways to extract data from dates in M._

I will take a look as some **Date() M** functions that can be used extract data from an existing date, for example, when I want to know the day or year of a particular date. I will give an example for each function.

**_Date.Day_**

**Date****.Day(datetime** **as** **datetime)** **as** **nullable number**

Returns the day for a **datetime** value.

This is a simple **M** function, which will extract the day of the month.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-597.jpg)

The **M** functionality I have used is

**\= Date.Day(\[Final Payment\])**

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-615.jpg)

The day of the month has now been extracted.

**_Date.DayOfWeek_**

**Date.DayOfWeek(**datetime **as any, optional** firstDayOfWeek **as nullable number) as nullable number** 

Returns a number between 0 and 6 representing the day of the week in the provided **datetime** value. This function takes an optional day value, **firstDayOfWeek**, to set the first day of the week for this relative calculation. Valid values are: **Day.Sunday**, **Day.Monday**, **Day.Tuesday**, **Day.Wednesday**, **Day.Thursday**, **Day.Friday**, and **Day.Saturday**.

I have not included the Microsoft help information about the default. The help says that the default is that the week starts on a Sunday, but when I tested it, the default is Monday! If I put a second parameter in, then I can indicate that the week should start on a Sunday (I can use **Day.Sunday** as the parameter). I might like to think that the week starts on a Friday, and I can set the function to agree with me, but I can’t think of a business reason to do this!

I will use the expense data for my fictional salespeople, to find out more about the date that I will be paying them their expenses.

![](<Base64-Image-Removed>)

I create a new custom column to show me the day.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-513.jpg)

The **M** formula I have used is

**\= Date.DayOfWeek(\[Final Payment\], Day.Sunday)**

I specified that the week starts on a Sunday.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-428.jpg)

I have my day of payment represented as a number, so that 0 is Sunday, 1 is Monday and so on.

**_Date.DayOfWeekName_**

**Date.DayOfWeekName(**date **as any, optional** culture **as nullable text)**

Returns the day of the week name for the provided **date** and, optionally, a **culture**.

An example of culture is ‘en-US’, to give me US English weekday names.

![](<Base64-Image-Removed>)

The **M** functionality I have used is

**\= Date.DayOfWeekName(\[Final Payment\])**

![](<Base64-Image-Removed>)

The name of the day is shown.

**_Date.DayOfYear_**

**Date****.DayOfYear(datetime** **as** **datetime)** **as** **nullable number**

Returns a number that represents the day of the year from a **datetime** value.

This will give me the day number within the year that the final payment takes place.

![](<Base64-Image-Removed>)

The **M** formula I have used is

**\= Date.DayOfYear(\[Final Payment\])**

![](<Base64-Image-Removed>)

I have the day number (in terms of the year) that my payment takes place.

**_Date.DaysInMonth_**

**Date****.DaysInMonth(datetime** **as** **datetime)** **as** **nullable number**

Returns the number of days in the month from a **datetime** value.

This function could be useful when comparing sales between months – if we are comparing July and February then it makes sense to take into account the number of days involved.

![](<Base64-Image-Removed>)

The **M** functionality I have used is

**\= Date.DaysInMonth(\[Final Payment\])**

![](<Base64-Image-Removed>)

The number of days in the month of the final payment is shown. There are a number of other extractions that I can do, and I have summarised all of them in the final image at the end of this blog.

**_Date.Year_**

**Date****.Year(datetime** **as** **datetime)** **as** **nullable number**

Returns the year from a **datetime** value.

An example **M** formula might be (used in the final image)

**\= Date.Year(\[Final Payment\])**

**_Date.Month_**

**Date****.Month(datetime** **as** **datetime)** **as** **nullable number**

Returns the month from a **datetime** value.

An example **M** formula might be (used in the final image)

**\= Date.Month(\[Final Payment\])**

**_Date.MonthName_**

**Date.MonthName(**date **as any, optional** culture **as nullable text)**

Returns the name of the month component for the provided `date` and, optionally, a **culture**.

An example **M** formula might be (used in the final image)

**\= Date.MonthName(\[Final Payment\])**

_**Date.QuarterOfYear**_

**Date****.QuarterOfYear(datetime** **as** **datetime)** **as** **nullable number**

Returns a number between 1 and 4 for the quarter of the year from a **datetime** value.

An example **M** formula might be (used in the final image)

**\= Date.QuarterOfYear(\[Final Payment\])**

**_Date.WeekOfMonth_**

**Date****.WeekOfMonth(datetime** **as** **datetime)** **as** **nullable number**

Returns a number for the count of week in the current month.

An example **M** formula might be (used in the final image)

**\= Date.WeekofMonth(\[Final Payment\])**

**_Date.WeekOfYear_**

**Date****.WeekOfYear(datetime** **as** **datetime)** **as** **nullable number**

Returns a number for the count of week in the current year.

An example **M** formula might be (used in the final image)

**\=Date.WeekOfYear(\[Final Payment\])**

This final screenshot shows all of the remaining functions:

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-getting-something-out-of-a-date/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-getting-something-out-of-a-date/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-getting-something-out-of-a-date/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-getting-something-out-of-a-date/#0)

[](https://sumproduct.com/blog/power-query-getting-something-out-of-a-date/#0 "close")

top
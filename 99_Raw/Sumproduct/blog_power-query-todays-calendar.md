# Power Query: Today’s Calendar

**Source:** https://sumproduct.com/blog/power-query-todays-calendar/

---

[Home](https://sumproduct.com/)

\> Power Query: Today’s Calendar

*   May 21, 2019

Power Query: Today’s Calendar
=============================

Power Query: Today’s Calendar
=============================

22 May 2019

_Welcome to our Power Query blog. Today, I am going to look at how to use the calendar table to filter on the current day._

I looked at how to create a calendar table a long time ago in [Power Query: Calendar Creation – Preparing for Dates](https://sumproduct.com/blog/power-query-calendar-creation-preparing-for-dates/)
 and [Power Query: Calendar Creation – Going for Dates](https://sumproduct.com/blog/power-query-calendar-creation-going-for-dates/)
. More recently, I looked at an example where I had a folder of expense files that had a date embedded in them, and I selected the ones that matched ‘today’ in [Power Query: Files for Today](https://sumproduct.com/blog/power-query-files-for-today/)
. The column I will add to my calendar table today provides another way to solve that issue, as I will show next time…

![](<Base64-Image-Removed>)

In order to see the query I used to generate this calendar, I can choose to ‘Show Queries’ from the ‘Get & Transform’ section on the ‘Data’ tab.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

I can edit my query by double-clicking on it, by right-clicking and selecting ‘Edit’ or by hovering over it and choosing ‘EDIT’ from the pop-up sample data screen.

![](<Base64-Image-Removed>)

I choose to add a ‘Custom Column’ from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Number.From(Date.From(DateTime.LocalNow()) – \[Date\])**

which gets the date from the current date and time, and then subtracts the **_Date_** value. The result is converted to a number. **Date.From** works in the local **timezone**, so this formula will work dynamically to give the difference between **_Date_** and the local date.

![](<Base64-Image-Removed>)

Next time I will use my Calendar query to filter expense files on today’s date.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-todays-calendar/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-todays-calendar/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-todays-calendar/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-todays-calendar/#0)

[](https://sumproduct.com/blog/power-query-todays-calendar/#0 "close")

top
# Number of Days in the Month

**Source:** https://sumproduct.com/thought/number-of-days-in-the-month/

---

[Home](https://sumproduct.com/)

\> Number of Days in the Month

*   May 14, 2025

Number of Days in the Month
===========================

How to work out how many times a particular day of the week occurs in a certain month.

Friday on My Mind
=================

Cyclicality is often an important element for forecasting modelling. Sometimes businesses need to know how many Fridays (or Saturdays, Sundays, etc.) there are in a particular month. But how do you calculate that? By Liam Bastick, Director with SumProduct Pty Ltd.

Query
-----

I am building a monthly forecasting model and, to assist, it is important to know how many Fridays there are in a particular month. Can this be calculated in Excel?

Advice
------

I often get asked by my clients “…can I do this?” or “…can I do that?” in Excel. I have yet to find something that Excel has not managed to solve. No doubt there’s a reader out there that can stump me!

Often, when building monthly forecasting models, one or more days of the week may be a key driver of analysis. For example, pubs and bars may find their highest takings are on Fridays and sporting events may have greater attendances at the weekends, etc. Therefore, modellers often need to know how many Fridays (say) there are in any particular month.

The answer is:

\=4+(DAY(DATE(Year, Month,35))<WEEKDAY(DATE(Year,Month,1)-Weekday\_Number))

However, I think I need to provide a little more explanation!

### The WEEKDAY() Function

To calculate this, I will need to use a particular Excel function, **WEEKDAY(Serial\_number,\[Return\_type\])**, which has the following arguments:

*   **Serial\_number** This is a required sequential number that represents the date of the day you are trying to find. Dates should be entered by using the DATE function, or as results of other formulas or functions. Problems can occur if dates are entered as text;
*   **Return\_type** This is a number that determines the type of return value. By default (or if not entered), this will return a value of 1 for Sunday, 2 for Monday, through to 7 for Saturday. I recommend not changing this default as this can cause problems with earlier versions of Excel.

But before I explain how this is used, let me explain my rationale for the calculation.

### The Five Week Month

The whole underlying concept revolves around the five week month. If there were five weeks / 35 days in each month, then it would not matter which day of the week you chose. There would be five Tuesdays, five Saturdays and so on. Similarly, if each month only had four weeks / 28 days, like a non-leap year February, any particular would occur four times in the month. The problem is, the number of days in the month lies between 28 and 31 days.

Therefore, I consider what “date” the 35th of a particular month is. For example, June has 30 days, so 35 June is actually 5 July, so the date would be 5. That means there would be two days of the week (7 – 5) that would occur five times in June, specifically whatever day 1 June and 2 June fall on.

Therefore **\=7-DAY(DATE(Year, Month,35))** tells us how many days of the week will occur five times for a given **Month** and **Year** (for more information on the **DAY()** and **DATE()** functions please see [Asking for a Date](https://www.sumproduct.com/thought/asking-for-a-date)
).

It is this idea I will expand upon.

**\=WEEKDAY(DATE(Year,Month,1))** tells me what day of the week the first day of a given **Month** and **Year** is. If it were Tuesday, for example, and **\=7-DAY(DATE(Year, Month,35))** is equal to 3, this would mean there were five Tuesdays, Wednesdays and Thursdays in that month (i.e. Tuesday 1, 8, 15, 22 and 29; Wednesday 2, 9, 16, 23 and 30; Thursday 3, 10, 17, 24 and 31).

I’m nearly there; the following formula gives us what we need.

\=4+(DAY(DATE(Year, Month,35))<WEEKDAY(DATE(Year,Month,1)-Weekday\_Number))

Let me explain:

*   The 4 at the beginning is the minimum number of occurrences of a particular day in any given month;
*   The remainder is a condition, which will either be TRUE or FALSE. Now 4+TRUE=5 whilst 4+FALSE=4, so this condition evaluates if the fifth occurrence will happen;
*   As discussed above, **DAY(DATE(Year, Month,35))** will give rise to a value of 4, 5, 6 or 7, depending upon whether there are 31, 30, 29 or 28 days in the month respectively. That is, for these numbers of days, there will be 3, 2, 1 or zero days which occur five times;
*   strong>If WEEKDAY(DATE(Year,Month,1)) is the **Weekday\_Number** of the day of the week being considered, then **DATE(Year,Month,1)-Weekday\_Number** will always return the date of the last Saturday of the prior month;
*   For example, 1 August 2012 is a Wednesday and it is the number of Wednesdays we want to count in August. The **Weekday\_Number** of Wednesday is 4; four days before 1 August 2012 is 28 July 2012, which is the last Saturday of the prior month; **WEEKDAY(28 July 2012)** is 7. **DAY(DATE(2012,8,35))** is 4, and since 4 < 7, there will be five Wednesdays in August 2012;
*   If the day of the week being considered is the second day of the given month, then **DATE(Year,Month,1)-Weekday\_Number** will always return the date of the last Friday of the prior month;
*   For example, 1 September 2012 is a Saturday and let me assume we are considering how many Sundays there are in September 2012 (i.e. Sunday is the second day of the month). The **Weekday\_Number** of Sunday is 1; one day before 1 September 2012 is 31 August 2012, which is the last Friday of the prior month; **WEEKDAY(31 August 2012)** is 6. **DAY(DATE(2012,9,35)) is 5**, and since 5 < 6, there will be five Sundays in September 2012;
*   Similarly, if the day of the week being considered is the third day of the given month, then **DATE(Year,Month,1)-Weekday\_Number** will always return the date of the last Thursday of the prior month;
*   For this final example, 1 November 2012 is a Thursday and let me assume we are considering how many Saturdays there are in November 2012 (i.e. Saturday is the third day of the month). The **Weekday\_Number** of Saturday is 7; seven days before 1 November 2012 is 25 October 2012, which is the last Thursday of the prior month; **WEEKDAY(25 October 2012)** is 5. **DAY(DATE(2012,11,35))** is also 5, and since 5 is not less than 5, there will only be four Saturdays in November 2012;
*   Hence this formula will count the number of occurrences of a particular weekday for a given month and year.

### A Word to the Wise…

There are several issues with the above formula:

*   The formula cited assumes **WEEKDAY()** is used with its default settings (Sunday = 1, Monday = 2, …, Saturday = 7). If this is changed, the formula will need to be revised accordingly;
*   The Earth goes around the sun once every 365.2422 days (I am available for trivia nights!) and hence not every fourth year is a leap year. If a year ends in ’00? (e.g. 2000), the year must be divisible by 400 – not four – to be a leap year. However, Excel’s dates / serial numbers do not work like this “…to be compatible with Lotus 1-2-3…” so this formula should only be used for months between January 1901 and December 2099. Hopefully, this is an acceptable limitation…;
*   Given how serial numbers differ between the Macintosh and Windows operating systems (again, please see [Asking for a Date](https://www.sumproduct.com/thought/asking-for-a-date)
    ), be careful of using this formula if end users will be using both of these systems;
*   And finally, please don’t write in to comment on the existence of hard code in the given formula. Regular readers will note I abhor hard code (other than 0 or 1) in formulae, but where a number cannot change (as here in two instances with 4 and 35), hopefully you will accept I “tolerate” this exception!

To assist with understanding this month’s article, please review the [attached Excel file](https://sumproduct.com/assets/thought-files/n-z/sp-number-of-xdays-in-a-month.xls)
 which contains a simple illustration of how this might work in practice.

![](<Base64-Image-Removed>)

Simple Example

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/number-of-days-in-the-month/#0)
    
*   [Register](https://sumproduct.com/thought/number-of-days-in-the-month/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/number-of-days-in-the-month/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/number-of-days-in-the-month/#0)

[](https://sumproduct.com/thought/number-of-days-in-the-month/#0 "close")

top
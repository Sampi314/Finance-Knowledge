# Power Pivot Principles: Irregular Month-End Reporting Case – Part 1

**Source:** https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-1/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Irregular Month-End Reporting Case – Part 1

*   August 17, 2020

Power Pivot Principles: Irregular Month-End Reporting Case – Part 1
===================================================================

Power Pivot Principles: Irregular Month-End Reporting Case – Part 1
===================================================================

18 August 2020

_Welcome back to the Power Pivot Principles blog. Over the next few weeks, we will cover a case study related to an irregular month-end reporting rule._

Consider we have a sales data set of four product lines in a supermarket over four years.

![](<Base64-Image-Removed>)

This supermarket has a rule for month-end reporting, which is the reporting end of month day is the final Thursday of a month, regardless of whether it matches the end of the calendar month.

First, we will load this data set to the Power Pivot Data Model, by highlighting the table, navigating to the Power Pivot tab on the Ribbon and click ‘Add to Data Model’:

![](<Base64-Image-Removed>)

Now, we will get the calendar end of month day using the **EOMONTH** function. Similar to the **EOMONTH** function in Excel, this function in DAX returns the date, in **datetime** format, for the last day of the month, before or after a specified number of months. The **EOMONTH** function can be used to calculate maturity dates or due dates that fall on the last day of the month. This function follows the syntax:

**EOMONTH(start\_date, months)**

where:

*   **start\_date** is the start date in **datetime** format, or in an accepted text representation of a date
*   **months** is the number representing the number of months before or after the **start\_date**. If the number entered is not an integer, the number is rounded up or down to the nearest integer.

In our Power Pivot Data Model, we will create a calculated column called ‘**End of Month**‘:

**\=EOMONTH(Sales\[Date\],0)**

![](<Base64-Image-Removed>)

We will create two more calculated columns that we may need later to work out our rules:

**Days to EOM = Sales\[End of Month\] – Sales\[Date\]**

![](<Base64-Image-Removed>)

**Final Week Flag = (Sales\[Days to EOM\]<=6)\*1**

![](<Base64-Image-Removed>)

Next, we need to calculate the day of the week for each date. This will allow us to determine the final Thursday. We will use the **WEEKDAY** function to this end.

The **WEEKDAY** function in DAX returns a number from one (1) to seven (7), identifying the day of the week from a date. By default, the day ranges from one (1 – Sunday) to seven (7 – Saturday). This function has the following syntax:

**WEEKDAY(date, return\_type)**

where:

*   **date** is a date in **datetime** format, which should be entered by the **DATE** function, by using expressions that result in a date, or as the result of other formulas
*   **return\_type** is the number that determines the Return value: **1** for week begins on Sunday (1) and ends on Saturday (7), numbered 1 through 7; **2** for week begins on Monday (1) and ends on Sunday (7); **3** for week begins on Monday (0) and ends on Sunday (6).

In our Power Pivot Data Model, we will create three calculated columns:

**Day of Week = WEEKDAY(Sales\[Date\],1)**

**Final Thursday Flag = (Sales\[Day of Week\]=5)\*Sales\[Final Week Flag\]**

**Day of Week EOM = WEEKDAY(Sales\[End of Month\],1)**

![](<Base64-Image-Removed>)

From these helper calculations, we can work out the ‘**Final Thursday**‘ day of that month at any point in time, based upon the logic of the weekday indicative number:

**\=IF(Sales\[Day of Week EOM\]>=5, Sales\[End of Month\] – (Sales\[Day of Week EOM\]-5),**

**Sales\[End of Month\] – (Sales\[Day of Week EOM\] + 7 – 5))**

![](<Base64-Image-Removed>)

Then, we will determine the ‘**Reporting End of Month**‘, where a **Date** larger than the ‘**Final Thursday**‘ belongs to next month’s ‘**End of Month**‘ day instead:

**\=IF(Sales\[Date\]>Sales\[Final Thursday\],EOMONTH(Sales\[Date\],1),Sales\[End of Month\])**

![](<Base64-Image-Removed>)

Alternatively, ‘Fill Up’ could have been used, but that’s a story for another time…

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-1/#0)

[](https://sumproduct.com/blog/power-pivot-principles-irregular-month-end-reporting-case-part-1/#0 "close")

top